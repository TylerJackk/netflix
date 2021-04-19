import json
from chalice import Chalice, Rate, Cron

from chalicelib.etl.converter import do_etl
from chalicelib.helper.send_notification import send_ifttt
from chalicelib.db_manager.constants import NF_ID_QUEUE, NF_ETL_QUEUE
from chalicelib.db_manager.s3_client import S3Client
from chalicelib.helper.utils import chunks
from chalicelib.scraper.constants import MOVIE, TV
from chalicelib.scraper.scraper import UnogsExplorer, UnogsScraper
from chalicelib.msg_queue.sqs import send_sqs_msg

app = Chalice(app_name="application")
app.debug = True


@app.on_sqs_message(queue=NF_ID_QUEUE, batch_size=1)
def scrape_nf_detail(event):
    """
    triggered by sqs event, scrape detail info by netflix id
    """
    for record in event:
        body = json.loads(record.body)
        nf_ids = body.get("nf_ids")
        resource_type = body.get("resource_type")
        batch = body.get("batch")
        scrape_type = body.get("scrape_type")
        s3_data = {}
        for nf_id in nf_ids:
            scraper = UnogsScraper(nf_id)
            s3_data[nf_id] = scraper.get_data()
        s3 = S3Client()
        # todo decouple s3 key and notification msg
        identifier = f"{scrape_type}_data-{batch}"
        key = s3.build_key(resource_type, identifier)
        s3.put(key, s3_data)
        send_ifttt(f"{resource_type} {identifier} saved to S3")


@app.route("/explore", methods=["GET"])
def explore_all_nf_data():
    """
    scrape all netflix data with pagination
    """
    request = app.current_request
    resource_type = request.query_params["resource_type"]
    offset = int(request.query_params["offset"])
    limit = int(request.query_params["limit"])
    explorer = UnogsExplorer(resource_type)
    success = explorer.explore(limit, offset)
    return {"success": success}


@app.route("/etl", methods=["GET"])
def trigger_etl_job():
    request = app.current_request
    resource_type = request.query_params["resource_type"]
    s3 = S3Client()
    object_key_list = s3.get_object_key_list(resource_type)
    for chunk in chunks(object_key_list, 10):
        send_sqs_msg(
            queue_name=NF_ETL_QUEUE,
            body={
                "s3_paths": chunk,
                "resource_type": resource_type,
            },
        )


@app.route("/{resource_type}/total", methods=["GET"])
def get_resource_total(resource_type):
    explorer = UnogsExplorer(resource_type)
    return {"total": explorer.get_total_resource_num()}


# Run at 10:00am (UTC) every day.
@app.schedule(Cron(0, 8, "*", "*", "?", "*"))
def explore_daily_new_resource():
    for resource_type in [TV, MOVIE]:
        explorer = UnogsExplorer(resource_type)
        explorer.search_new_resource()


@app.on_sqs_message(queue=NF_ETL_QUEUE, batch_size=1)
def etl(event):
    """
    triggered by sqs event, convert S3 raw data and load to ES
    """
    for record in event:
        body = json.loads(record.body)
        resource_type = body.get("resource_type")
        s3_paths = body.get("s3_paths")
        for s3_path in s3_paths:
            do_etl(s3_path, resource_type)
            send_ifttt(f"{s3_path} loaded to ES")

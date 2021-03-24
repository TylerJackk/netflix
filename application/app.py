import json
from chalice import Chalice

from chalicelib.helper.send_notification import send_ifttt
from chalicelib.db_manager.constants import NF_ID_QUEUE
from chalicelib.db_manager.s3_client import S3Client
from chalicelib.scraper.scraper import UnogsExplorer, UnogsScraper

app = Chalice(app_name="application")
app.debug = True


@app.on_sqs_message(queue=NF_ID_QUEUE, batch_size=1)
def scrape_nf_detail(event):
    for record in event:
        body = json.loads(record.body)
        nf_ids = body.get("nf_ids")
        resource_type = body.get("resource_type")
        batch = body.get("batch")
        s3_data = {}
        for nf_id in nf_ids:
            scraper = UnogsScraper(nf_id)
            s3_data[nf_id] = scraper.get_data()
        s3 = S3Client()
        key = s3.build_key(resource_type, f"data-{batch}")
        s3.put(key, s3_data)
        message = f"{resource_type} data(batch {batch}) saved to S3"
        send_ifttt(message)


@app.route("/explore", methods=["GET"])
def explore_all_nf_data():
    request = app.current_request
    resource_type = request.query_params["resource_type"]
    offset = int(request.query_params["offset"])
    limit = int(request.query_params["limit"])
    explorer = UnogsExplorer(resource_type)
    success = explorer.explore(limit, offset)
    return {"success": success}


@app.route("/{resource_type}/total", methods=["GET"])
def get_resource_total(resource_type):
    explorer = UnogsExplorer(resource_type)
    return {"total": explorer.get_total_resource_num()}

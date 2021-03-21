import json
from chalice import Chalice

from chalicelib.db_manager.constants import NF_ID_QUEUE
from chalicelib.db_manager.s3_client import S3Client
from chalicelib.scraper.scraper import UnogsExplorer, UnogsScraper

app = Chalice(app_name="application")
app.debug = True


@app.on_sqs_message(queue=NF_ID_QUEUE, batch_size=1)
def scrape_nf_detail(event):
    for record in event:
        body = json.loads(record.body)
        nf_id = body.get("nf_id")
        resource_type = body.get("resource_type")
        scraper = UnogsScraper(nf_id)
        data = scraper.get_data()
        s3 = S3Client()
        key = s3.build_key(resource_type, nf_id)
        return s3.put(key, data)


@app.route("/explore", methods=["GET"])
def explore_all_nf_data():
    request = app.current_request
    resource_type = request.query_params["resource_type"]
    offset = int(request.query_params["offset"])
    explorer = UnogsExplorer(resource_type)
    success = explorer.explore(offset)
    return {"success": success}


@app.route("/{resource_type}/total", methods=["GET"])
def get_resource_total(resource_type):
    explorer = UnogsExplorer(resource_type)
    return {"total": explorer.get_total_resource_num()}

import json

from chalice import Chalice

from chalicelib.db_manager.s3_client import S3Client
from chalicelib.scraper.constants import TV, MOVIE
from chalicelib.scraper.scraper import UnogsExplorer, UnogsScraper
from chalicelib.db_manager.constants import NF_ID_QUEUE

app = Chalice(app_name="application")
app.debug = True


@app.on_sqs_message(queue=NF_ID_QUEUE, batch_size=1)
def scrape_nf_detail(event):
    for record in event:
        body = json.loads(record.body)
        nf_id = body.get('nf_id')
        resource_type = body.get('resource_type')
        scraper = UnogsScraper(nf_id)
        data = scraper.get_data()
        s3 = S3Client()
        key = s3.build_key(resource_type, nf_id)
        return s3.put(key, data)


@app.route("/explore", methods=["GET"])
def explore_all_nf_data():
    for resource_type in [TV, MOVIE]:
        u = UnogsExplorer(resource_type)
        u.explore()

import json
from app import app
from chalice.test import Client

from chalicelib.db_manager.constants import NF_ID_QUEUE


def test_scrape_detail():
    with Client(app) as client:
        response = client.lambda_.invoke(
            "scrape_nf_detail",
            client.events.generate_sqs_event(
                message_bodies=[
                    json.dumps({"nf_id": 81422699, "resource_type": "movie"})
                ],
                queue_name=NF_ID_QUEUE,
            ),
        )
        assert response.payload == True


def test_explore_all_nf_data():
    with Client(app) as client:
        response = client.http.get("/explore?offset=0&resource_type=movie")
        assert response.json_body == {"success": True}


def test_get_resource_total():
    resource_type = "movie"
    with Client(app) as client:
        response = client.http.get(f"/{resource_type}/total")
        assert response.json_body.get("total") != None

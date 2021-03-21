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

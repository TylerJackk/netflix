import boto3
import json

from chalicelib.db_manager.constants import REGION, NF_ID_QUEUE


def send_sqs_msg(queue_name, body):
    """
    send message to AWS SQS
    """
    body = json.dumps(body)
    sqs = boto3.resource("sqs", region_name=REGION)
    queue = sqs.get_queue_by_name(QueueName=NF_ID_QUEUE)
    resp = queue.send_message(MessageBody=body)
    return resp["ResponseMetadata"]["HTTPStatusCode"] == 200

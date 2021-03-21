import boto3
import pickle
from chalicelib.db_manager.constants import NF_BUCKET, REGION
from datetime import datetime


class S3Client(object):
    def __init__(self, bucket=NF_BUCKET, region=REGION):
        self.bucket = bucket
        self.region = region

    @property
    def client(self):
        s3 = boto3.resource("s3", region_name=self.region)
        return s3

    def create_bucket(self, bucket_name):
        bucket_response = self.client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": self.region},
        )
        return bucket_name, bucket_response

    @staticmethod
    def build_key(resource_type, nf_id):
        """
        build s3 key
        pattern: '/Movie/2021-03-18/nf_id.json'
        :param resource_type:
        :param nf_id:
        :return:
        """
        current_date_str = datetime.now().strftime("%Y-%m-%d")
        return f"{resource_type}/{current_date_str}/{nf_id}.json"

    def _build_s3_object(self, key):
        return self.client.Object(self.bucket, key)

    def get(self, key):
        s3_object = self._build_s3_object(key)
        body = s3_object.get()["Body"].read()
        return pickle.loads(body)

    def put(self, key, body):
        s3_object = self._build_s3_object(key)
        serialized_body = pickle.dumps(body)
        resp = s3_object.put(Body=serialized_body)
        if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return True
        return False

    def delete(self, key):
        s3_object = self._build_s3_object(key)
        print(s3_object.delete())

import json

import boto3
import pendulum

from chalicelib.db_manager.constants import NF_BUCKET, REGION


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
    def build_key(country_code, resource_type, index):
        """
        build s3 key
        pattern: 'UK/Movie/2021-03-18/1.json'
        :param country_code:
        :param resource_type:
        :param index:
        :return:
        """
        now_str = pendulum.now().format("YYYY-MM-DD")
        return f"{country_code}/{resource_type}/{now_str}/{index}.json"

    def _build_s3_object(self, key):
        return self.client.Object(self.bucket, key)

    def get(self, key):
        s3_object = self._build_s3_object(key)
        data = s3_object.get()["Body"].read()
        return json.loads(data)

    def put(self, key, body):
        s3_object = self._build_s3_object(key)
        resp = s3_object.put(Body=json.dumps(body))
        print(resp)

    def delete(self, key):
        s3_object = self._build_s3_object(key)
        print(s3_object.delete())


# if __name__ == '__main__':
#     s3 = S3Client()
#     s3.delete('test-123')

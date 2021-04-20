import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

from chalicelib.db_manager.constants import ES_HOST, ES_TEMPLATE_PREFIX, ES_REGION
from chalicelib.scraper.constants import MOVIE, TV


class ESConnection(object):
    def __init__(self):
        self._conn = None

    def get_conn(self):
        if self._conn is None:
            self._conn = self._get_conn_by_boto()
        return self._conn

    def _get_conn_by_boto(self):
        """
        get es connection by boto(AWS specific)
        """
        service = "es"
        credentials = boto3.Session().get_credentials()
        aws_auth = AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            ES_REGION,
            service,
            session_token=credentials.token,
        )
        self._conn = Elasticsearch(
            hosts=[{"host": ES_HOST, "port": 443}],
            http_auth=aws_auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
        )
        return self._conn

    def _get_conn(self):
        """
        common way to get es connection
        :return:
        """
        self._conn = Elasticsearch(
            hosts=[ES_HOST],
            scheme="https",
            port=443,
        )
        return self._conn


class ESClient(object):
    def __init__(self):
        self.es = ESConnection().get_conn()

    @property
    def movie_index(self):
        return f"{ES_TEMPLATE_PREFIX}-{MOVIE}"

    @property
    def tv_index(self):
        return f"{ES_TEMPLATE_PREFIX}-{TV}"

    def create_index(self, index_name, body=None):
        if not self.es.indices.exists(index_name):
            self.es.indices.create(index_name, body=body)

    def delete_index(self, index_name):
        self.es.indices.delete(index_name)

    def put(self, index_name, data):
        nf_id = data["nf_id"]
        body = data["body"]
        self.es.index(index_name, body=body, id=nf_id)

    def search(self, index, body, routing=None, ignore_unavailable=True):
        res = self.es.search(
            index=index,
            body=body,
            routing=routing,
            request_timeout=30,
            ignore_unavailable=ignore_unavailable,
        )
        return res

    def msearch(self, body):
        res = self.es.msearch(body=body)
        return res

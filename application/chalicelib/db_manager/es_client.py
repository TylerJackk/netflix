from elasticsearch import Elasticsearch

from chalicelib.db_manager.constants import ES_HOST, ES_TEMPLATE_PREFIX
from chalicelib.db_manager.es_template import TEMPLATE
from chalicelib.scraper.constants import MOVIE, TV


class ESConnection(object):
    def __init__(self):
        self._conn = None

    def get_conn(self):
        if self._conn is None:
            self._conn = self._get_conn()
        return self._conn

    def _get_conn(self):
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

    def create_index(self, index_name):
        if not self.es.indices.exists(index_name):
            self.es.indices.create(index_name)

    def put_template(self):
        for template_name, template in TEMPLATE.items():
            if self.es.indices.exists_template(template_name):
                self.es.indices.delete_template(template_name)
            self.es.indices.put_template(name=template_name, body=template)

    def delete_index(self, index_name):
        self.es.indices.delete(index_name)

    def put(self, index_name, data):
        nf_id = data["nf_id"]
        body = data["body"]
        self.es.index(index_name, body=body, id=nf_id)

    def search(self, index, body, routing, ignore_unavailable=True):
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

from dataclasses import dataclass

from chalicelib.db_manager.es_client import ESClient


class ESReader(object):
    def __init__(self, es_param=None):
        self.param = es_param
        self.client = ESClient()

    @property
    def default_search_index(self):
        return "netflix-v2*"

    def _build_country_code_query(self):
        """
        build search by country codes query clause
        country_code : 'AU', 'HK'
        :return: country code query clause
        """
        if not self.param.country_code:
            return
        query_clause = {
            "bool": {
                "must": [
                    {"match": {"country_info.country_code": self.param.country_code}},
                ]
            }
        }
        return query_clause

    def _build_subtitle_query(self):
        """
        build search by subtitles query clause
        subtitles: list of subtitle ['Simplified Chinese','ENGLISH']
        :return: subtitle query clause
        """
        if not self.param.subtitles:
            return
        should_clause = [
            {"match": {"country_info.subtitle": subtitle}}
            for subtitle in self.param.subtitles
        ]
        query_clause = {"bool": {"should": should_clause}}
        return query_clause

    def _build_resource_type_query(self):
        if not self.param.resource_type:
            return
        return {"term": {"vtype": self.param.resource_type}}

    def _build_date_query(self):
        if not self.param.start_date or not self.param.end_date:
            return
        query_clause = {
            "range": {
                "release_date": {
                    "gte": self.param.start_date,
                    "lte": self.param.end_date,
                    "format": "yyyy-MM-dd",
                }
            }
        }
        return query_clause

    def _build_nested_query(self):
        """
        :return:
        """
        if not self.param.country_code and not self.param.subtitles:
            return {}
        nested_query = {
            "nested": {
                "path": "country_info",
                "query": {
                    "bool": {
                        "must": [
                            self._build_country_code_query(),
                            self._build_subtitle_query(),
                        ],
                    }
                },
            }
        }
        return nested_query

    @staticmethod
    def clean_up_empty_filter(query):
        query["query"]["bool"]["filter"] = [
            item for item in query["query"]["bool"]["filter"] if item
        ]
        query["query"]["bool"]["must"] = [
            item for item in query["query"]["bool"]["must"] if item
        ]
        return query

    def build_query(self):
        """
        build ES query by parameters
        """
        query = {
            "track_total_hits": True,
            "query": {
                "bool": {
                    "filter": [
                        self._build_resource_type_query(),
                        self._build_date_query(),
                    ],
                    "must": [
                        {"match": {"title": self.param.title}},
                        self._build_nested_query(),
                    ],
                },
            },
        }
        return self.clean_up_empty_filter(query)

    def search(self):
        """
        doc
        :return:
        """
        query = self.build_query()
        resp = self.client.search(self.default_search_index, body=query)
        hits = resp["hits"]["hits"]
        return hits


@dataclass
class ESParameter:
    """
    This dataclass is to store all params which is to build request to ES.
    """

    title: str
    release_year: str = None
    resource_type: str = None
    start_date: str = None
    end_date: str = None
    country_code: str = None
    subtitles: list = None

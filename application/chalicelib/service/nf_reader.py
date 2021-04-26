from chalicelib.service.es_reader import ESReader


class NFReader(object):
    def __init__(self, es_param):
        self.es_param = es_param
        self.es_reader = ESReader(es_param)

    def build_response(self):
        hits = self.es_reader.search()
        result = []
        for hit in hits:
            source = hit["_source"]
            title = source["title"]
            synopsis = source["synopsis"]
            available_country_codes = [
                info["country_code"] for info in source["country_info"]
            ]
            result.append(
                {
                    "title": title,
                    "synopsis": synopsis,
                    "available_country_codes": available_country_codes,
                }
            )

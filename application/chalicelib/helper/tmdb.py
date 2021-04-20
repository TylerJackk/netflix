import copy

import requests

from chalicelib.constants import TMDB_API_KEY

LANGUAGE = "zh"
TMDB_URL = "https://api.themoviedb.org/3"
SEARCH_URL = TMDB_URL + "/search/"
SEARCH_PEOPLE = "/search/person"
BASE_PAYLOAD = {"api_key": TMDB_API_KEY, "language": "zh"}
RESOURCE_TYPE_MAPPING = {"series": "tv", "movie": "movie"}


class TMDBClient(object):
    """
    The Movie Database API Client
    """

    def __init__(self, resource_type):
        self.resource_type = RESOURCE_TYPE_MAPPING.get(resource_type, resource_type)

    def search(self, name):
        search_endpoint = SEARCH_URL + self.resource_type
        payload = copy.deepcopy(BASE_PAYLOAD)
        payload.update({"query": name})
        resp = requests.get(search_endpoint, params=payload)
        if resp.status_code == 200:
            results = resp.json().get("results", [])
            if len(results) >= 1:
                return results[0]
            else:
                raise ValueError("No Match found")
        return None

    def get_detail(self, video_id):
        detail_endpoint = TMDB_URL + f"/{self.resource_type}/{video_id}"
        resp = requests.get(detail_endpoint, params=BASE_PAYLOAD)
        if resp.status_code == 200:
            return resp.json()

    def get_cast(self, video_id):
        cast_endpoint = TMDB_URL + f"/{self.resource_type}/{video_id}/credits"
        resp = requests.get(cast_endpoint, params=BASE_PAYLOAD)
        if resp.status_code == 200:
            return resp.json()

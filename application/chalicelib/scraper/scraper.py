import time

import json
import requests
from decimal import Decimal

from chalicelib.msg_queue.sqs import send_sqs_msg
from chalicelib.scraper.constants import (
    SEARCH,
    HEADERS,
    COUNTRY_CODE_ID_MAPPING,
    DETAIL,
    BGIMAGES,
    GENRES,
    PEOPLE,
    ACTOR,
    CREATOR,
    COUNTRIES,
    EPISODES,
    STATIC_INFO,
    MOVIE,
    TV,
)


class UnogsScraper:
    """
    scrape data by nf_id
    """

    def __init__(self, nf_id=None):
        self.nf_id = nf_id

    @property
    def payload(self):
        return {"netflixid": self.nf_id}

    def get_detail(self):
        res = requests.get(url=DETAIL, params=self.payload)
        data = res.json()
        if len(data) == 0:
            return {}
        return data

    def get_images(self):
        res = requests.get(url=BGIMAGES, params=self.payload)
        data = res.json()
        if len(data) == 0:
            return {}
        return data

    def get_genres(self):
        res = requests.get(url=GENRES, params=self.payload)
        genres = [genre["genre"] for genre in res.json()]
        return genres

    def get_cast(self):
        res = requests.get(url=PEOPLE, params=self.payload)
        actors = []
        creators = []
        if res.status_code == 200:
            data = res.json()
            for item in data:
                if item["type"] == ACTOR:
                    actors = [x["fullname"] for x in item["arr"]]
                if item["type"] == CREATOR:
                    creators = [x["fullname"] for x in item["arr"]]
        return {"actors": actors, "creators": creators}

    def get_country(self):
        res = requests.get(url=COUNTRIES, params=self.payload)
        return res.json()

    def get_episodes(self):
        res = requests.get(url=EPISODES, params=self.payload)
        return res.json()

    def get_data(self):
        detail = self.get_detail()
        images = self.get_images()
        cast = self.get_cast()
        country = self.get_country()
        episode = self.get_episodes()
        genres = self.get_genres()
        item_data = {
            "nf_id": self.nf_id,
            "detail": detail,
            "images": images,
            "cast": cast,
            "country": country,
            "episode": episode,
            "genres": genres,
        }
        # convert float to Decimal
        item_data_dump = json.dumps(item_data)
        item = json.loads(item_data_dump, parse_float=Decimal)
        return item


class UnogsExplorer:
    """
    explore nf_id by search
    """

    def __init__(self, resource_type):
        self.resource_type = resource_type

    @property
    def country_list(self):
        country_code_list = [str(code) for code in COUNTRY_CODE_ID_MAPPING.values()]
        return ",".join(country_code_list)

    def search_resource(self, limit=100, offset=0):
        payload = {
            "limit": limit,
            "offset": offset,
            "query": "",
            "countrylist": self.country_list,
            "country_andorunique": "or",
            "start_year": "1900",
            "end_year": "2021",
            "start_rating": "",
            "end_rating": "10",
            "genrelist": "",
            "type": self.resource_type,
            "audio": "",
            "subtitle": "",
            "audiosubtitle_andor": "or",
            "person": "",
            "filterby": "",
            "orderby": "",
        }
        response = requests.get(url=SEARCH, headers=HEADERS, params=payload)
        if response.status_code == 200:
            return response.json()

    def explore(self):
        """
        explore all data on unogos website and send nf_id to SQS
        """
        # only query from first page return 'total'
        total = self.search_resource().get("total")
        for offset in range(0, total // 100 + 1):
            time.sleep(5)
            resources = self.search_resource(offset=offset)["results"]
            for resource in resources:
                nf_id = resource.get("nfid")
                if nf_id:
                    send_sqs_msg({"nf_id": nf_id})


class UnogsStaticScraper:
    """
    scrape static data(eg. country info,language info)
    """

    def get_static_data(self):
        resp = requests.get(url=STATIC_INFO)
        country_info_list = resp.json()["countries"]["results"]
        language_static_list = resp.json()["languages"]
        self.parse_country_info(country_info_list)

    @staticmethod
    def parse_country_info(country_info_list):
        country_id_mapping = {}
        country_code_id_mapping = {}
        for info in country_info_list:
            country_id_mapping.update({info["country"]: info["id"]})
            country_code_id_mapping.update({info["countrycode"]: info["id"]})
        print(country_id_mapping)
        print(country_code_id_mapping)


if __name__ == "__main__":
    for resource_type in [TV, MOVIE]:
        u = UnogsExplorer(resource_type)
        u.explore()
        # send_sqs_msg('test')

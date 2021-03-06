from datetime import datetime

from chalicelib.db_manager.es_client import ESClient
from chalicelib.db_manager.es_mapping import ES_MAPPING
from chalicelib.db_manager.s3_client import S3Client
from chalicelib.helper.tmdb import TMDBClient
from chalicelib.scraper.constants import TV, MOVIE


def setup(rebuild_index=False):
    es = ESClient()
    if rebuild_index:
        es.delete_index(es.tv_index)
        es.delete_index(es.movie_index)
    es.create_index(es.tv_index, ES_MAPPING["series"])
    es.create_index(es.movie_index, ES_MAPPING["movie"])


class Converter(object):
    """
    Transform raw data to ES format
    """

    def __init__(self, resource_type):
        self.resource_type = resource_type

    @property
    def tmdb(self):
        return TMDBClient(self.resource_type)

    def build_tmdb_data(self, title):
        try:
            tmdb_data = self.tmdb.search(title)
        except Exception:
            return None, None, None
        tmdb_id = tmdb_data["id"]
        tmdb_detail = self.tmdb.get_detail(tmdb_id)
        tmdb_title = tmdb_data.get("title")
        tmdb_synopsis = tmdb_detail.get("overview")
        return tmdb_id, tmdb_title, tmdb_synopsis

    @staticmethod
    def _build_country_info(country_data):
        country_info = []
        for country in country_data:
            audios = country["audio"].split(",")
            subtitles = country["subtitle"].split(",")
            info = {
                "country_code": country["cc"],
                "audio": audios,
                "subtitle": subtitles,
            }
            country_info.append(info)
        return country_info

    @staticmethod
    def _build_season_info(season_data):
        season_info = []
        for season in season_data:
            data = {"season": season["season"]}
            episodes = []
            for episode in season.get("episodes"):
                episode_info = {
                    "ep_id": episode["epid"],
                    "ep_num": episode["epnum"],
                    "season_num": episode["seasnum"],
                    "synopsis": episode["synopsis"],
                    "title": episode["title"],
                    "img": episode["img"],
                }
                episodes.append(episode_info)
            data["episodes"] = episodes
            season_info.append(data)
        return season_info

    @staticmethod
    def _build_images(images):
        image_info = {}
        for key, value in images.items():
            image_info[key] = value[0]
        return image_info

    def build_es_data(self, data):
        nf_id = data.get("nf_id")
        detail = data.get("detail")[0]
        imdb_id = detail.get("imdbid")
        release_date = detail.get("nfdate")
        nf_title = detail.get("title")
        nf_synopsis = detail.get("synopsis")
        vtype = detail.get("vtype")
        # genres
        genres = data.get("genres")
        year = detail.get("year")
        # cast
        cast = data.get("cast")
        nf_actors = cast.get("actors")
        nf_creators = cast.get("creators")
        country_info = self._build_country_info(data.get("country"))
        images = self._build_images(data.get("images"))
        tmdb_id, tmdb_title, tmdb_synopsis = self.build_tmdb_data(nf_title)
        es_data = {
            "nf_id": nf_id,
            "body": {
                "tmdb_id": tmdb_id,
                "imdb_id": imdb_id,
                "release_date": release_date,
                "title": [nf_title, tmdb_title],
                "synopsis": [nf_synopsis, tmdb_synopsis],
                "vtype": vtype,
                "genres": genres,
                "year": year,
                "actors": nf_actors,
                "creators": nf_creators,
                "images": images,
                "country_info": country_info,
                "created_time": datetime.now(),
            },
        }
        if self.resource_type == TV:
            season_info = self._build_season_info(data.get("episode"))
            es_data["body"]["season_info"] = season_info
        return es_data


def do_etl(s3_key, resource_type):
    """
    Extract raw data from S3
    Transform raw data to ES format
    Load data to ES
    """
    s3 = S3Client()
    es = ESClient()
    es_resource_index_mapping = {TV: es.tv_index, MOVIE: es.movie_index}
    convert = Converter(resource_type)
    raw_data = s3.get(s3_key)
    for _id, resource in raw_data.items():
        es_data = convert.build_es_data(resource)
        es.put(es_resource_index_mapping[resource_type], es_data)


if __name__ == "__main__":
    # setup()
    do_etl("movie/2021-04-26/daily_scrape_data-0.json", "movie")

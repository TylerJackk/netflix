ES_MAPPING = {
    "movie": {
        "mappings": {
            "_source": {"enabled": True},
            "properties": {
                "tmdb_id": {"type": "integer"},
                "nf_id": {"type": "integer"},
                "imdb_id": {"type": "keyword"},
                "release_date": {"type": "date"},
                "title": {
                    "type": "text",
                    "fields": {"suggest": {"type": "completion"}},
                },
                "synopsis": {"type": "keyword"},
                "vtype": {"type": "keyword"},
                "generes": {"type": "integer"},
                "year": {"type": "integer"},
                "actors": {"type": "text"},
                "creators": {"type": "text"},
                "images": {"type": "object"},
                "country_info": {
                    "type": "nested",
                    "properties": {
                        "country_code": {"type": "keyword"},
                        "audio": {"type": "keyword"},
                        "subtitle": {"type": "keyword"},
                    },
                },
                "created_time": {"type": "date"},
            },
        }
    },
    "series": {
        "mappings": {
            "_source": {"enabled": True},
            "properties": {
                "tmdb_id": {"type": "integer"},
                "nf_id": {"type": "integer"},
                "imdb_id": {"type": "keyword"},
                "release_date": {"type": "date"},
                "title": {
                    "type": "text",
                    "fields": {"suggest": {"type": "completion"}},
                },
                "synopsis": {"type": "keyword"},
                "vtype": {"type": "keyword"},
                "generes": {"type": "integer"},
                "year": {"type": "integer"},
                "actors": {"type": "text"},
                "creators": {"type": "text"},
                "images": {"type": "object"},
                "country_info": {
                    "type": "nested",
                    "properties": {
                        "country_code": {"type": "keyword"},
                        "audio": {"type": "keyword"},
                        "subtitle": {"type": "keyword"},
                    },
                },
                "season_info": {"type": "nested"},
                "created_time": {"type": "date"},
            },
        }
    },
}

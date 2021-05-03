# get country_code count
query = {
    "aggs": {
        "country_info": {
            "nested": {"path": "country_info"},
            "aggs": {
                "code_count": {
                    "terms": {"field": "country_info.country_code", "size": 100}
                }
            },
        }
    }
}

# get audio count
query1 = {
    "aggs": {
        "country_info": {
            "nested": {"path": "country_info"},
            "aggs": {
                "code_count": {"terms": {"field": "country_info.audio", "size": 100}}
            },
        }
    }
}
# get subtitle count
query3 = {
    "aggs": {
        "country_info": {
            "nested": {"path": "country_info"},
            "aggs": {
                "code_count": {"terms": {"field": "country_info.subtitle", "size": 100}}
            },
        }
    }
}

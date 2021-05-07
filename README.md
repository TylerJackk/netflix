## Features
* Scraping data from Unogos website
  * historical scraping for all data
  * daily scraping new data
* Raw data storage and ETL
  * save raw data to S3
  * S3 -> ETL -> ElasticSearch
* Backend service providing search ability

## Usage
Base URL for all endpoints: `https://w7lpq44qz8.execute-api.ap-east-1.amazonaws.com/api/`

### Search Resource

Endpoint

`GET /search`

Query parameters

| Parameter     | Type   | Limit                   | Description                        | Required |
| ------------- | ------ | ----------------------- | ---------------------------------- | -------- |
| title         | string | `1 <= len(title) <= 20` | Resource title your want to search | True     |
| resource_type | string | `series`, `movie`       | Specify resource type              | False    |
| country_code  | string | supported country code  | Specify country code               | False    |

Example request

````shell
$ http get https://w7lpq44qz8.execute-api.ap-east-1.amazonaws.com/api/search\?title\='mank'
````
Example response

```shell
{
    "result": [
        {
            "available_country_codes": [
                "AR",
                "AU",
                "BE",
                "BR",
                "CA",
                "CO",
                "CZ",
                "FR",
                "DE",
                "GR",
                "HK",
                "HU",
                "IS",
                "IN",
                "IL",
                "IT",
                "JP",
                "LT",
                "MY",
                "MX",
                "NL",
                "PL",
                "PT",
                "RO",
                "RU",
                "SG",
                "SK",
                "ZA",
                "KR",
                "ES",
                "SE",
                "CH",
                "TH",
                "TR",
                "GB",
                "US"
            ],
            "synopsis": [
                "1930s Hollywood is reevaluated through the eyes of scathing wit and alcoholic screenwriter Herman J. Mankiewicz as he races to finish “Citizen Kane.”",
                "　　随着赫尔曼·J·曼凯维奇争分夺秒地完成奥逊·威尔斯的《公民凯恩》剧本，人们将通过这位尖刻的社会评论家兼嗜酒编剧的视角，重新审视 20 世纪 30 年代的好莱坞。"
            ],
            "title": [
                "MANK",
                "曼克"
            ]
        }
    ]
}
```



## Tech

![](https://img.shields.io/badge/Python-3.9.2-blue)

**built with**
* AWS Lambda
* AWS SQS
* AWS S3
* AWS ElasticService(ElasticSearch)
* Chalice
* The Movie Database SDK

## Project Structure
```
.
├── README.md
├── application # chalice project root dir
│   ├── __pycache__
│   │   └── app.cpython-39.pyc
│   ├── app.py # all lambda function
│   ├── chalicelib # config files and additional application modules
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── constants.py
│   │   ├── db_manager # storage manager
│   │   ├── etl # ETL releated code
│   │   ├── helper
│   │   ├── msg_queue
│   │   ├── scraper 
│   │   └── service # Backend Service
│   ├── requirements.txt # deployment env requirements
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       └── test_app.py
├── requirements.txt # dev env requirements
└── scrape.py
```
## Project Title
This Project is aim to scraping Netflix resource info and provide RESTful API.

## Features
* Scraping data from Unogos website
  * historical scraping for all data
  * daily scraping new data
* Raw data storage and ETL
  * save raw data to S3
  * S3 -> ETL -> ElasticSearch
* Backend service providing search ability

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

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Requirements
```bigquery
python 3.9.0b5
```
## Project Structure
```
.
├── README.md
└── application # chalice project root dir
    ├── app.py # all route information
    ├── chalicelib # config files and additional application modules
    │   ├── __init__.py
    │   └── constants.py
    └── requirements.txt

```



## Storage

### S3
raw data from unogs
```
#/Bucket/Region/Resource_type/data_by_date
#/my-netflix-bucket/HK/Movie/2021-03-17-1
```

### Elasticsearch
converted data

S3 ---> ES(ETL)
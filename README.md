
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
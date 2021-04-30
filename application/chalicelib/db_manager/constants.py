# AWS RELATED CONSTANTS
REGION = "ap-east-1"
# ========== S3 settings ====
NF_BUCKET = "netflix-raw-data"

# ========== ES settings ====
ES_HOST = (
    "search-netflix-data-zp4wrfi3rxyj55kxpc2ssurfqu.ap-southeast-1.es.amazonaws.com"
)
ES_TEMPLATE_PREFIX = "netflix-v2-resource"
ES_REGION = "ap-southeast-1"
ES_DOMAIN_NAME = "netflix-data"

# ========== SQS settings ====
NF_ID_QUEUE = "netflix-id"
NF_ETL_QUEUE = "netflix-etl"

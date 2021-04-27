import requests

"""
nohup python -u scrape.py > output.log &
"""
RESOURCE_TYPES = ["series", "movie"]

API_URL = "https://w7lpq44qz8.execute-api.ap-east-1.amazonaws.com/api/"


def scrape():
    for resource_type in RESOURCE_TYPES:
        resp = requests.get(f"{API_URL}{resource_type}/total/")
        total = resp.json()["total"]
        print(f"=====Start crawling {resource_type}=====")
        print(f"total count: {total}")
        for offset in range(total // 50 + 1):
            print(offset)
            resp = requests.get(
                f"{API_URL}explore?limit=50&offset={offset * 50}&resource_type={resource_type}"
            )
            if resp.json()["success"]:
                print(f"offset {offset} explore triggered")
            import time

            time.sleep(60)


def trigger_etl():
    for resource_type in RESOURCE_TYPES:
        api = f"{API_URL}etl?resource_type={resource_type}"
        resp = requests.get(api)
        if resp.status_code == 200:
            print(f"{resource_type} etl triggered")


if __name__ == "__main__":
    trigger_etl()

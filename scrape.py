import requests

"""
nohup python -u scrape.py > output.log &
"""
RESOURCE_TYPES = ["series", "movie"]


def scrape():
    for resource_type in RESOURCE_TYPES:
        resp = requests.get(
            f"https://w7lpq44qz8.execute-api.ap-east-1.amazonaws.com/api/{resource_type}/total/"
        )
        total = resp.json()["total"]
        print(f"=====Start crawling {resource_type}=====")
        print(f"total count: {total}")
        for offset in range(total // 100 + 1):
            print(offset)
            resp = requests.get(
                f"https://w7lpq44qz8.execute-api.ap-east-1.amazonaws.com/api/explore?offset={offset * 100}&resource_type={resource_type}"
            )
            if resp.json()["success"]:
                print(f"offset {offset} explore triggered")
            import time

            time.sleep(60)


if __name__ == "__main__":
    scrape()

import requests

RESOURCE_TYPES = ["series", "movie"]


def scrape():
    for resource_type in RESOURCE_TYPES:
        resp = requests.get(
            f"https://w7lpq44qz8.execute-api.ap-east-1.amazonaws.com/api/{resource_type}/total/"
        )
        total = resp.json()["total"]
        for offset in range(total // 100 + 1):
            resp = requests.get(
                f"https://w7lpq44qz8.execute-api.ap-east-1.amazonaws.com/api/explore?offset={offset}&resource_type={resource_type}"
            )


if __name__ == "__main__":
    scrape()

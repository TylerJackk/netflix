import requests

EVENT = "NF Notification"


def send_ifttt(msg, event=EVENT):
    url = f"https://maker.ifttt.com/trigger/{event}/with/key/bDL5IbC1VbAsSr2xWvuTLC"
    data = {"value1": msg}
    requests.post(url, data=data)

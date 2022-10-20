import requests
import os
import time
from helper_funcs.API_keys import getKey
from requests import Response
from urllib.parse import urlencode
from user_agent import generate_user_agent

sc_cookie = getKey("sc_cookie")
user_agent = generate_user_agent()

# [0] = Daily, [1] = 4h
iValues = ['p55738127392', 'p57289512688']

def get_chart(symbol, tf):
    if tf == '1d':
        selector = 0
    if tf == '4h':
        selector = 1

    millisecondsEpoch = str(int(time.time()*1000))

    # [0] = Daily, [1] = 4h
    payloadObjects = [
        {"s": symbol, "p": "D", "b": "6", "g": '0', 'i': iValues[selector], 'r': millisecondsEpoch},
        {"s": symbol, "p:": "195", "b": "6", "g": "0", "i": iValues[selector], 'r': millisecondsEpoch}
    ]

    encoded_payload = urlencode(
            payloadObjects[selector]
        )
    
    url = f"https://stockcharts.com/c-sc/sc?{encoded_payload}"
    response = stockCharts_request(url, user_agent)
    fileName = download_chart_image(response, url)
    return fileName

def stockCharts_request(url: str, user_agent: str) -> Response:
    response = requests.get(url, headers={
        "cookie": sc_cookie, 
        "User-Agent": user_agent
    })
    return response

def download_chart_image(page_content: requests.Response, url,):
    """ Downloads a .png image of a chart into the "charts" folder. """
    file_name = f"{url.split('s=')[1].split('&')[0]}_{int(time.time())}.png"

    with open(os.path.join("/Library/WebServer/Documents/charts/test-charts", file_name), "wb") as handle:
        handle.write(page_content.content)
    
    return file_name

import requests
from bs4 import BeautifulSoup
import json
import datetime


def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}</h3>"
        output += f"날씨 : {loc.select_one('wf').string}<br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn').string}/{loc.select_one('tmx').string}<hr>"

    return output

def get_weather_house():
    API_KEY = 'WheJyyqo3FCeVxffSHIZaNl0WjWHm6OhSYvI8gfisQ8ObqBocgqjemN%2BboAwgbf2wwgw5pFuCrVPf2Nmkce5OA%3D%3D'
    API_KEY_decode = requests.utils.unquote(API_KEY)
    print(API_KEY_decode)
    return API_KEY_decode
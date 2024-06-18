from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, request
import requests
import json

app = Flask(__name__)


@app.route('/')  # root 경로
def hello():
    return 'Hello, Flask!!!!'


@app.route('/name')
def hello1():
    return 'Hello, 곰돌이 사육사!!!!'


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'stations': ['강남역', '역삼역', '서울역'],
        'ridership': [1000, 800, 1200]
    }
    response = Response(json.dumps(data, ensure_ascii=False), mimetype='application/json; charset=utf-8')
    return response


@app.route('/api/weather', methods=['GET'])
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


# Get 요청시 쿼리파라미터 사용하기
@app.route('/api/query', methods=['GET'])
def get_query():
    output = ""
    item_type = request.args.get('type', default=None, type=str)
    item_color = request.args.get('color', default=None, type=str)
    output += f"<h1>{item_type}</h1>"
    output += f"<h1>{item_color}</h1>"
    return output

# 경로변수 사용하기
@app.route('/api/item/<item_id>', methods=['GET'])
def get_path_item(item_id):
    output =""
    output += f"<h1>{item_id}</h1>"
    return output

@app.route('/api/register', methods=['POST'])
def post_register():
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)
    return jsonify({"username": username, "password": password})

if __name__ == '__main__':
    app.run()

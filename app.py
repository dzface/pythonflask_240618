from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, request
import requests
import json


from routers.data import get_data
from routers.weather import get_weather, get_weather_house


app = Flask(__name__)

@app.route('/')  # root 경로
def hello():
    return 'Hello, Flask!!!!'


@app.route('/name')
def hello1():
    return 'Hello, 곰돌이 사육사!!!!'





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

# add_url_rule 사용하여 라우트 추가
app.add_url_rule('/api/data', 'get_data_route', get_data, methods=['GET'])
app.add_url_rule('/api/weather', 'get_weather_route', get_weather, methods=['GET'])
app.add_url_rule('/api/weather-house', 'get_weather_house', get_weather_house, methods=['GET'])

if __name__ == '__main__':
    app.run()

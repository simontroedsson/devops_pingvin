from flask import Flask, render_template, url_for, request
from get_data import getHourlyWeatherData
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    API_KEY = os.getenv('API_KEY')
    return render_template('index.html',data=getHourlyWeatherData(latitude=59.3293,longitude=18.0686,API_KEY=API_KEY,units='metric'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

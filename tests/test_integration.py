import pytest
import os
import requests
from dotenv import load_dotenv

load_dotenv()
latitude = 59.3293
longitude = 18.0686
units = "metric"
API_KEY = os.getenv('API_KEY')

if API_KEY == None:
    raise ValueError("API key not found")

def test_getHourlyWeatherData():
    try:
        url = f"http://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={API_KEY}&units={units}"
        response = requests.get(url)
        response.raise_for_status()
        assert response.status_code == 200, f"Error status code: {response.status_code}"
        data = response.json()
        assert 'hourly' in data, f"Incorrect data format"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"API call failed: {e}")
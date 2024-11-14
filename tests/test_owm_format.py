from dotenv import load_dotenv
import os
load_dotenv()
from get_data import getHourlyWeatherData, latitude, longitude, units
from datetime import datetime


API_KEY = os.getenv('API_KEY')

def test_per_hour_data_structure():
    perHourData = getHourlyWeatherData(latitude, longitude, API_KEY, units)
    assert isinstance(perHourData, list)
    assert len(perHourData) > 0
    for entry in perHourData:
        assert isinstance(entry, dict)
        assert "Date" in entry
        assert isinstance(entry["Date"], str)
        assert bool(datetime.strptime(entry["Date"], "%Y-%m-%d"))
        assert "Time" in entry
        assert isinstance(entry["Time"], str)
        assert bool(datetime.strptime(entry["Time"], "%H:%M:%S"))
        assert "Temperature" in entry
        assert isinstance(entry["Temperature"], int)
        assert "Weather" in entry
        assert isinstance(entry["Weather"], str)
        assert "Windspeed m/s" in entry
        assert isinstance(entry["Windspeed m/s"], (float,int))
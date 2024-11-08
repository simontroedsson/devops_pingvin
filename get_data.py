import requests
import datetime
import os

latitude = 59.3293
longitude = 18.0686
units = "metric"
API_KEY = os.getenv('API_KEY')


def getHourlyWeatherData(latitude, longitude, API_KEY, units):
    response = requests.get(f"http://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={API_KEY}&units={units}")
    owmData = response.json()
    perHour = []

    for hour in owmData["hourly"]:    
        dateAndTime = hour["dt"]
        utcDateTime = datetime.datetime.fromtimestamp(dateAndTime, tz=datetime.timezone.utc)
        swedishTime = utcDateTime + datetime.timedelta(hours=1)
        formattedDate = swedishTime.strftime("%Y-%m-%d")
        formattedTime = swedishTime.strftime("%H:%M:%S")
        temperature = hour["temp"]
        description = hour["weather"][0]["main"]
        windspeed = hour["wind_speed"]

        perHour.append({"Date": formattedDate, "Time": formattedTime, "Temperature": round(temperature), "Weather": description, "Windspeed m/s": round(windspeed, 1)})
        if len(perHour) == 25:
            perHour = perHour[1:]
            break
    return perHour
        
        
perHourData = getHourlyWeatherData(latitude, longitude, API_KEY, units)
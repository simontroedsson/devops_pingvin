import requests
import datetime
import os

latitude = 59.3293
longitude = 18.0686
units = "metric"

API_KEY = os.getenv('')
API_KEY = "29612899e6d6265a3cacae00393aa263"
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

    perHour.append([formattedDate, formattedTime, round(temperature), description, round(windspeed, 1)])
for i in perHour:
    print(i)
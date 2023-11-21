import requests
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv("API_KEY")
MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"


weather_parameter = {
    "lat": 7.3045033,
    "lon": 5.1412033,
    "appid": API_KEY,
    "units": 'metric',
    "exclude": 'current,minutely,daily'
}

response = requests.get(
    url=OWM_Endpoint, params=weather_parameter)
response.raise_for_status()
waether_data = response.json()
weather_slice = waether_data['hourly'][:12]


will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject:WeatherCondition\n\nBring an umbrella")

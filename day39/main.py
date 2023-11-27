# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint

endpoint = "https://api.sheety.co/9e8f4da9e713d31f33c5798b7f6dff05/copyOfFlightDeals/prices"

response = requests.get(url=endpoint)
response.raise_for_status()
sheet_data = response.json()["prices"]

pprint(sheet_data)

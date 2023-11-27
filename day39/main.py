# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch


endpoint = "https://api.sheety.co/9e8f4da9e713d31f33c5798b7f6dff05/copyOfFlightDeals/prices"


response = requests.get(url=endpoint)
response.raise_for_status()
sheet_data = response.json()["prices"]

FlightSearch(sheet_data)
print(sheet_data)

import requests
from flight_search import FlightSearch
import json


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = f"https://api.sheety.co/9e8f4da9e713d31f33c5798b7f6dff05/flightDeals/prices/"
        self.headers = {
            "Content-Type": "application/json"
        }

    def get_sheet_data(self):
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        self.data = response.json()["prices"]
        return self.data

    def put_sheet_data(self):
        for data in self.get_sheet_data():
            iataCode = FlightSearch(data["city"]).get_iata_code()
            sheet_body = json.dumps({'price': {'iataCode': iataCode}})
            response = requests.put(url=f"{self.endpoint}{
                                    data['id']}", data=sheet_body, headers=self.headers)
            if response.status_code != 200:
                print(response.content)
            response.raise_for_status()

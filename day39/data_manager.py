import requests
from flight_search import FlightSearch
from flight_data import FlightData
import json

# headers_sheety = { "Authorization": MY AUTHORIZATION HEADER, }

# sheety_response = requests.post(
# url=ENDPOINT, json=new_workout_data, headers=headers_sheety)

# Authorization: Basic ZW1tYTpkZGRzW2Rsdm1sZA==


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = f"https://api.sheety.co/9e8f4da9e713d31f33c5798b7f6dff05/copyOfFlightDeals/prices/"
        self.bearer_headers = {"Authorization": "Bearer sfl;mflbmflmflfm"}

    def get_sheet_data(self):
        response = requests.get(url=self.endpoint)
        response.raise_for_status()
        self.data = response.json()["prices"]
        return self.data

    def put_sheet_data(self):
        for data in self.get_sheet_data():
            iataCode = FlightSearch(data["city"]).get_iata_code()
            sheet_body = {"price": {"iataCode": iataCode}}
            url = f"{self.endpoint}{data['id']}"
            response = requests.put(
                url, json=sheet_body, headers=self.bearer_headers)
            response.raise_for_status()
    



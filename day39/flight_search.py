import requests


class FlightSearch():
    def __init__(self, cityName):
        self.cityName = cityName
        self.headers = {"apikey": "X_HScQ8shTDBuFXxRTmZiREEhHiHlqjs"}
        self.endpoint = f"https://api.tequila.kiwi.com/locations/query?term={self.cityName}"

    def get_iata_code(self):
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        data = data['locations'][0]['code']
        return data

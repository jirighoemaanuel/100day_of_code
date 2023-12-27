import requests
import datetime
from datetime import datetime, timedelta


class FlightData:
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    six_months = today + timedelta(days=180)

    tomorrow_str = tomorrow.strftime("%Y-%m-%d")
    six_months_str = six_months.strftime("%Y-%m-%d")

    def __init__(self, fly_to, arrival_city):
        self.departure_city = "Lagos"
        self.departure_city_code = "LOS"
        self.arrival_city = arrival_city
        self.arrival_city_code = fly_to
        self.params = {
            "fly_from": self.departure_city_code,
            "fly_to": self.arrival_city_code,
            "date_from": FlightData.tomorrow_str,
            "date_to": FlightData.six_months_str
        }
        self.headers = {
            "apikey": "X_HScQ8shTDBuFXxRTmZiREEhHiHlqjs"
        }

    def check_flight_data(self):
        response = requests.get(
            url=f"https://api.tequila.kiwi.com/search", params=self.params, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return (self.departure_city, self.departure_city_code, self.arrival_city, self.arrival_city_code, data['data'][1]['price'])

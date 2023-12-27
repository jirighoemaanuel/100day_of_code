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

        # Unix timestamps from your JSON
        dTime_unix = data['data'][0]['dTime']
        aTime_unix = data['data'][0]['aTime']

        # Convert to datetime objects
        dTime_dt = datetime.utcfromtimestamp(dTime_unix)
        aTime_dt = datetime.utcfromtimestamp(aTime_unix)

        # Format the datetime objects as strings with year-month-day format
        dTime_str = dTime_dt.strftime('%Y-%m-%d %I:%M:%S %p UTC')
        aTime_str = aTime_dt.strftime('%Y-%m-%d %I:%M:%S %p UTC')

        flightdata = {"departure_city": self.departure_city, "departure_city_code": self.departure_city_code,
                      "arrival_city": self.arrival_city, "arrival_city_code": self.arrival_city_code, "price": data['data'][1]['price'], "dTime": dTime_str, "aTime": aTime_str}
        return flightdata

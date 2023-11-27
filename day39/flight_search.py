class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, sheet_data):
        self.sheet_data = sheet_data
        self.get_city_iata()

    def get_city_iata(self):
        for data in self.sheet_data:
            data['iataCode'] = "Testing"

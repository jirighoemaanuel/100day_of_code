# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirement
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager


sheet = DataManager()
sheet_data = sheet.get_sheet_data()
for data in sheet_data:
    flightdata = FlightData(data["iataCode"], data["city"])
    flightdata.check_flight_data()



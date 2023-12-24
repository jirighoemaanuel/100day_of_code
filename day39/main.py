# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirement
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager


sheet = DataManager()
sheet_data = sheet.get_sheet_data()
sheet.put_sheet_data()


pprint(sheet_data.get_sheet_data())

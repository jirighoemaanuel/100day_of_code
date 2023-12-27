# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirement
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

import smtplib
import os

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")


sheet = DataManager()
sheet_data = sheet.get_sheet_data()
for data in sheet_data:
    flightdata = FlightData(data["iataCode"], data["city"]).check_flight_data()
    flightdata
    if int(data["lowestPrice"]) <= flightdata["price"]:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Alert! Flight Deals\n\nLow price alert! Only {flightdata['price']} to fly from {
                                    flightdata['departure_city']}-{flightdata['departure_city_code']} to {flightdata['arrival_city']}-{flightdata['arrival_city_code']}, from {flightdata['dTime']} to {flightdata['aTime']}.")


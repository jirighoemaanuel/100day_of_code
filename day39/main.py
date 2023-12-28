from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

import smtplib
import os

MY_EMAIL = os.getenv("EMAIL")
MY_PASSWORD = os.getenv("PASSWORD")



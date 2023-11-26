import requests
from datetime import datetime
import os


USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"
GRAPHID = 'graph'


user_params = {
    "token": TOKEN,
    "username": {USERNAME},
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Coding Time",
    "unit": "minute",
    'type': "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime(year=2023, month=11, day=24)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120",
}

response = requests.post(url=pixel_creation_endpoint,
                         json=pixel_data, headers=headers)
print(response.text)

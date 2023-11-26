import requests
import os
import json


APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
exercise = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json",
}

body = {
    'query': exercise,
}

body_json = json.dumps(body)

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=endpoint, data=body_json, headers=headers)
response.raise_for_status()
data = response.text
print(data)

import requests
import os


APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

headers = {
    "x-app=id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json",
}

body = {
    'query': "ran 1km for 20min",
    "gender": "male",
    "age": "22"
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=endpoint, body=body, headers=headers)
response.raise_for_status()
data = response.text
print(data)

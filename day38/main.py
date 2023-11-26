import requests
import os
import json
import datetime

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')
exercise = input("Tell me which exercises you did: ")
sheet_endpoint = "https://api.sheety.co/9e8f4da9e713d31f33c5798b7f6dff05/copyOfMyWorkouts/workouts"

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json",
}

sheet_headers = {
    "Content-Type": "application/json"
}

exercise_body = {
    'query': exercise,
}

body_json = json.dumps(exercise_body)

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=endpoint, data=body_json,
                         headers=exercise_headers)
response.raise_for_status()
data = response.json()["exercises"]
exercise_data = [[info["duration_min"],
                  info["nf_calories"], info["name"]] for info in data]


for info in data:
    duration, calories, exercise_name = info["duration_min"], info["nf_calories"], info["name"]
    exercise_data = json.dumps({
        "workout": {
            "date": datetime.datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise_name.title(),
            "duration": duration,
            "calories": calories,
        }
    })
    resp = requests.post(url=sheet_endpoint, data=exercise_data,
                         headers=sheet_headers)
    resp.raise_for_status()
    print(resp.text)

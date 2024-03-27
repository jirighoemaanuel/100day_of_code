from flask import Flask, render_template
import random
import requests

app = Flask(__name__)


@app.route('/<name>')
def home(name):

    genderize_response = requests.get(f"https://api.genderize.io/?name={name}")
    gender = genderize_response.json().get("gender")
    agify_response = requests.get(f"https://api.agify.io/?name={name}")
    age = agify_response.json().get("age")
    user = name.title()
    return render_template("index.html", gender=gender, age=age, name=user)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def blog():
    response = requests.get("https://api.npoint.io/471904fd18302b1232a6")
    blog_data = response.json()
    print(blog_data)
    return render_template("index.html", blogs=blog_data)

@app.route('/post/<id>')
def post():
    

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def blog():
    response = requests.get("https://api.npoint.io/471904fd18302b1232a6")
    blog_data = response.json()
    return render_template("index.html", blogs=blog_data)


@app.route('/post/<post_id>')
def post(post_id):
    response = requests.get("https://api.npoint.io/471904fd18302b1232a6")
    blog_data = response.json()
    post_data = blog_data[int(post_id) - 1]
    return render_template("post.html", post=post_data)


if __name__ == "__main__":
    app.run(debug=True)

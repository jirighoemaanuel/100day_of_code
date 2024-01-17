from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<strong>{function()}<strong>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"


@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)

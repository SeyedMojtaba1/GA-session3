"""Add flask module for create API"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def say_hello():
    """Function for test"""
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)

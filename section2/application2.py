from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/davidn")
def davidn():
    return "Hello, David Nunez"

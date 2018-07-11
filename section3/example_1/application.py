from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # https://www.w3schools.com/python/python_datetime.asp
    tm = datetime.datetime.now()

    return render_template("index.html", date=str(tm))
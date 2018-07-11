### How to use sessions:
# http://flask.pocoo.org/docs/1.0/quickstart/#sessions

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

app.secret_key = os.urandom(12)


@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"


@app.route("/login", methods=["POST"])
def do_admin_login():
    if request.form["password"] == "password" and request.form["username"] == "admin":
        session["logged_in"] = True
    else:
        print("wrong password!")
    return home()


@app.route("/logout")
def logout():
    session["logged_in"] = False
    return home()

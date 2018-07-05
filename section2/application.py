from flask import Flask

app = Flask(__name__)

# decorator saying that the function below it, is
# what you are calling should your route ("/") be true
@app.route("/")
def index():
    return "Hello, world!"

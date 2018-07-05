from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "hello, world!"


# saying take any string and pass that into the function
@app.route("/<string:name>")
def say_hello(name):
    return "Hello, {}!".format(name)


@app.route("/post/<int:post_id>")
def something(post_id):
    # show the post with the given id, the id is an integer
    return "Post %d" % post_id


@app.route("/returnJSON")
def post_json():
    obj = {"item1": "value1", "item2": "value2"}
    # we half to jsonify the dictionary else we will get thrown an error
    # i recommend to try removing the "jsonify()" to see the error you get
    return jsonify(obj)

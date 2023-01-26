from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "ok"


app.run("0.0.0.0", 9000)
from flask import Flask

app = Flask(__name__)


@app.route("/")
def cookie_manager():
    return "ok"


if __name__ == '__main__':
    app.run("0.0.0.0", 9000)
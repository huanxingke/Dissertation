from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    if request.method == "GET":
        return "This is HuanXingke's Vercel API for dissertation."
    else:
        return {"code": 200, "msg": "This is HuanXingke's Vercel API for dissertation."}


@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
@app.errorhandler(503)
def handle_error(err_msg):
    if request.method == "GET":
        return f"""
        <h1>Error!</h1>
        <h2>{err_msg}</h2>
        <h2>{request.url}</h2>
        <h2>By HuanXingke</h2>
        """
    else:
        return {"code": -1, "msg": str(err_msg)}


if __name__ == '__main__':
    app.run("0.0.0.0", 9000)
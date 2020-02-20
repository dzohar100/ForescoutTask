from flask import jsonify, Flask

app = Flask(__name__)


def hello200ok():
    resp = jsonify(success=True)
    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0:8080", debug=True)
hello200ok()

import flask
import requests
import torch
import numpy as np

app = flask.Flask(__name__)


@app.route("/ml", methods=["POST"])
def get_prediction():
    jsn = flask.request.json["data"]
    # redis queue push and watch pattern
    if is_testing_user(current_user):
        r = requests.post("http://localhost:8080/v1.2/submit", json=jsn, timeout=2)
    else:
        r = requests.post("http://localhost:8080/v1.1/submit", json=jsn, timeout=2)
    return str(r.json())


if __name__ == "__main__":
    app.run(port=5000)

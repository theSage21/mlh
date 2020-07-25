import flask
import torch
import numpy as np
from . import model

app = flask.Flask(__name__)
net = model.Net()
net.load_state_dict(torch.load("mnist_cnn.pt"))
net.eval()


@app.route("/ml", methods=["POST"])
def get_prediction():
    jsn = flask.request.json["data"]
    x = torch.Tensor(np.array(jsn).reshape(1, 1, 28, 28))
    y = net.forward(x).detach().numpy().flatten()
    return str(y)


if __name__ == "__main__":
    app.run(port=5000)

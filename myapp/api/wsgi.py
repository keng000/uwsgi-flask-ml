import torch
from flask import Flask

from myapp.ml.model import Net
from myapp.path import PathManager

app = Flask(__name__)

# Model pre-loading
net = Net()
model_path = PathManager.MODELS / "model.pth"
net.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage))
net.eval()


@app.route("/estimate", methods=["GET"])
def estimate():
    dummy = torch.rand(1, 3, 32, 32)
    net(dummy) # <- here, the process will stuck

    return "OK", 200


@app.route("/health", methods=["GET"])
def health():
    return "alive", 200

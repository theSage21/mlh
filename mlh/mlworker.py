from . import model
from time import sleep
import torch
from tqdm import tqdm
import numpy as np
import requests
from itertools import repeat

net = model.Net()
net.load_state_dict(torch.load("mnist_cnn.pt"))
net.eval()

url = "http://localhost:8080"
with requests.Session() as s:
    for _ in tqdm(repeat([None])):
        batch = []
        jids = []
        for _ in range(32):
            try:
                r = s.get(f"{url}/work", timeout=2)
            except Exception as e:
                break
            else:
                data = r.json()["data"]
                batch.append(np.array(data).reshape(1, 28, 28))
                jids.append(r.json()["jobid"])
        if not batch:
            continue
        if len(batch) == 1:
            batch = batch[0].reshape(1, 1, 28, 28)
        else:
            batch = np.vstack(batch).reshape(len(batch), 1, 28, 28)
        print(batch.shape)  # B, 1, 28, 28
        print(batch.shape)  # B, 1, 28, 28
        print(batch.shape)  # B, 1, 28, 28
        print(batch.shape)  # B, 1, 28, 28
        y = net.forward(torch.Tensor(batch)).detach().numpy()
        s.post(f"{url}/work", json={"jobids": jids})
        batch, jids = [], []

import time
import requests
from itertools import repeat
from tqdm import tqdm
from torchvision import datasets
import numpy as np

dataset1 = datasets.MNIST("./data", train=False, download=True)
examples = []
for image, target in dataset1:
    arr = np.array(image).flatten().astype(float)
    examples.append({"data": list(arr)})
url = "http://localhost:5000"

with requests.Session() as s:
    with tqdm() as pbar:
        while True:
            for d in examples:
                try:
                    r = s.post(f"{url}/ml", json=d)
                except:
                    time.sleep(1)
                else:
                    pbar.update(1)

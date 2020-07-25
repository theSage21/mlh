from time import sleep
import requests
from itertools import repeat
from tqdm import tqdm

url = "http://localhost:8080"
d = {"a": 1, "b": 2}

with requests.Session() as s:
    for _ in tqdm(repeat([None])):
        batch = []
        jids = []
        for _ in range(32):
            r = s.get(f"{url}/work")
            data = r.json()
            a, b = data["data"].pop("a"), data["data"].pop("b")
            batch.append((a, b))
            jids.append(data["jobid"])
            if len(batch) > 10:
                results = [a + b for a, b in batch]
                sleep(1)
                s.post(f"{url}/work", json={"jobids": jids})
                batch, jids = [], []

from time import sleep
import requests
from itertools import repeat
from tqdm import tqdm

url = "http://localhost:8080"
d = {"a": 1, "b": 2}

with requests.Session() as s:
    for _ in tqdm(repeat([None])):
        r = s.get(f"{url}/work")
        data = r.json()
        a, b = data["data"].pop("a"), data["data"].pop("b")
        data["result"] = a + b
        sleep(1)
        s.post(f"{url}/work", json=data)

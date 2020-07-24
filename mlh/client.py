import requests
from itertools import repeat
from tqdm import tqdm

url = "http://localhost:8080"
d = {"a": 1, "b": 2}

with requests.Session() as s:
    for _ in tqdm(repeat([None])):
        r = s.post(f"{url}/submit", json=d)

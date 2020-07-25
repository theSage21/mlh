import requests
from itertools import repeat
from tqdm import tqdm

url = "http://localhost:8080"
d = {"a": 1, "b": 2}

with requests.Session() as s:
    with tqdm() as pbar:
        for _ in repeat([None]):
            try:
                r = s.post(f"{url}/submit", json=d, timeout=2)
            except:
                pass
            else:
                pbar.update(1)

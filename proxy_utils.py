import random
import os

def get_proxy():
    path = "proxies.txt"
    if os.path.exists(path):
        with open(path, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
            if proxies:
                return random.choice(proxies)
    return None

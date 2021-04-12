from typing import Tuple, Dict

import requests

def make_request_non_deterministic(endpoint:str)->Tuple[int, Dict]:
    result = requests.get(endpoint)
    return result.status_code, result.json()


def run():
    print(make_request_non_deterministic("http://0.0.0.0:8080/random"))


def main():
    for i in range(10):
        run()

if __name__ == "__main__":
    main()

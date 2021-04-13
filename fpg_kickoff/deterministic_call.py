from typing import Optional, Dict

import requests
from requests import Response


class MyAwesomeResult:
    def __init__(self, status_code: int, raw_content: str, json: Optional[Dict] = None):
        self.status_code = status_code
        self.raw_content = raw_content
        self.json = json

    @classmethod
    def from_response(cls, response: Response):
        try:
            json = response.json()
        except ValueError:
            json = None
        return MyAwesomeResult(response.status_code, response.text, json)


def make_deterministic_call(endpoint: str) -> Response:
    return requests.get(endpoint)


def make_deterministic_call_2(endpoint: str) -> MyAwesomeResult:
    return MyAwesomeResult.from_response(requests.get(endpoint))


def run():
    result = make_deterministic_call("http://0.0.0.0:8080/random")
    print(f"Result 1: {result.status_code} -> {result.text}")
    result2 = make_deterministic_call_2("http://0.0.0.0:8080/random")
    print(f"Result 2: {result2.status_code} -> {result2.json}")
    print("-----")


def main():
    for i in range(10):
        run()


if __name__ == "__main__":
    main()

import random
from typing import Optional
from returns.maybe import Maybe


def divide_things(x: int, y: int) -> Optional[float]:
    if y == 0:
        return None
    return x / y


def run():
    num = random.randint(-1, 1)
    denom = random.randint(-1, 10)
    Maybe.from_optional(divide_things(num, denom)).map(print)

def main():
    for i in range(100):
        run()

if __name__ == "__main__":
    main()

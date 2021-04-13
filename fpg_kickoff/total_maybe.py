import random
from returns.maybe import Maybe, Some, Nothing


def divide_things(x: int, y: int) -> Maybe[float]:
    if y == 0:
        return Nothing
    return Some(x / y)


def run():
    num = random.randint(-1, 1)
    denom = random.randint(-1, 10)
    divide_things(num, denom).map(print)


def main():
    for i in range(100):
        run()


if __name__ == "__main__":
    main()

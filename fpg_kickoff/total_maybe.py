import random
from returns.maybe import Maybe, Some, Nothing


def ultra_complex_operation(x: int, y: int) -> Maybe[float]:
    if y == 0:
        return Nothing
    return Some(x / y)


def main():
    for i in range(100):
        num = random.randint(-1, 1)
        denom = random.randint(-1, 10)
        ultra_complex_operation(num, denom).map(print)


if __name__ == "__main__":
    main()

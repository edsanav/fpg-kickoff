import random


def divide_things(x: int, y: int) -> float:
    return x / y


def run():
    num = random.randint(-1, 1)
    denom = random.randint(-1, 10)
    result = divide_things(num, denom)
    print(result)


def main():
    for i in range(100):
        run()


if __name__ == "__main__":
    main()
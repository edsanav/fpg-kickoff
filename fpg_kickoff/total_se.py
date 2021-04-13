import random


def ultra_complex_operation(x: int, y: int) -> float:
    return x / y


def main():
    for i in range(100):
        num = random.randint(-1, 1)
        denom = random.randint(-1, 10)
        result = ultra_complex_operation(num, denom)
        print(result)

if __name__ == "__main__":
    main()

import random
from typing import List


def get_combination(n:int) -> List[int]:
    return [random.randint(0,9) for _ in range(n)]


def run():
    result_1 = get_combination(10)
    print(result_1)
    result_2 = get_combination(10)
    print(result_2)


def main():
    run()


if __name__ == "__main__":
    main()

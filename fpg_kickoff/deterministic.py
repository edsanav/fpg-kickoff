import random
from typing import List


def get_combination(n: int, state: object) -> List[int]:
    random.setstate(state)
    return [random.randint(0, 9) for _ in range(n)]


def main():
    state = random.getstate()
    result_1 = get_combination(10, state)
    print(result_1)
    result_2 = get_combination(10, state)
    print(result_2)


if __name__ == "__main__":
    main()

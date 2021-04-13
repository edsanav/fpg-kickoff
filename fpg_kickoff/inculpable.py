def count_letter(content: str, letter: str) -> int:
    return content.count(letter)


def main():
    print(count_letter("/tmp/this/does/not_exists", "a"))


if __name__ == "__main__":
    main()

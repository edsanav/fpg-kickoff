

def unsafe():
    ...

def count_letter(content:str, letter:str)->int:
    return content.count(letter)

def run():
    print(count_letter("/tmp/this/does/not_exists", "a"))


def main():
    run()


if __name__ == "__main__":
    main()

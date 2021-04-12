
def count_letter(filepath:str, letter:str)->int:
    with open(filepath) as fd:
        content = fd.read()
        return content.count(letter)

def run():
    print(count_letter("/tmp/this/does/not_exists", "a"))


def main():
    run()


if __name__ == "__main__":
    main()

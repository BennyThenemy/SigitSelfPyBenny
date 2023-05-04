def numbers_letters_count(my_str):
    digits = 0
    letters = 0
    for char in my_str:
        if char.isdigit():
            digits += 1
        else:
            letters += 1
    return [digits, letters]


def main():
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == '__main__':
    main()
    
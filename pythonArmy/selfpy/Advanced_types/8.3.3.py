def count_chars(my_str):
    returned_dict = {}
    for char in my_str:
        if char != ' ':
            if char in returned_dict:
                returned_dict[char] = returned_dict[char] + 1
            else:
                returned_dict[char] = 1

    return returned_dict


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))


if __name__ == '__main__':
    main()

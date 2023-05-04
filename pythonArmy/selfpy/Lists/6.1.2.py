def shift_left(my_list):
    shifted_list = [my_list[1], my_list[2], my_list[0]]
    return shifted_list


def main():
    shifted_list = shift_left(["smart", "you", "are"])
    print(shifted_list)


if __name__ == '__main__':
    main()

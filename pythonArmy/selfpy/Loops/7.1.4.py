def squared_numbers(start, stop):
    my_list = list()
    while start <= stop:
        my_list.append(pow(start, 2))
        start += 1

    return my_list


def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))


if __name__ == '__main__':
    main()

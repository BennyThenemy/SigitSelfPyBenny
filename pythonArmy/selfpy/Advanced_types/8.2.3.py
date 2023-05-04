def mult_tuple(tuple1, tuple2):
    pairs = []
    for key1 in tuple1:
        for key2 in tuple2:
            pairs.append((key1, key2))
            pairs.append((key2, key1))
    return tuple(pairs)


def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))


if __name__ == '__main__':
    main()

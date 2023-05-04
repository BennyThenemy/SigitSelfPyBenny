def extend_list_x(list_x, list_y):
    for item in list_x:
        list_y.append(item)
    return list_y


def main():
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(extend_list_x(x, y))


if __name__ == '__main__':
    main()

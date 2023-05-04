def seven_boom(end_number):
    boom_list = list()
    for num in range(0, end_number+1):

        if num % 7 == 0 or str(num).__contains__(str(end_number)):
            boom_list.append("BOOM")
            continue

        boom_list.append(num)

    return boom_list


def main():
    print(seven_boom(17))


if __name__ == '__main__':
    main()

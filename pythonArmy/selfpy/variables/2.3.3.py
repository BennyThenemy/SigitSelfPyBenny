if __name__ == '__main__':
    my_input = input("Enter three digits (each digit for one pig): ")

    # digits sum:
    my_input_list = map(int, list(my_input))
    sum = sum(my_input_list)
    print(sum)
    # dividing:
    print(int(sum/3))
    # remainder in number:
    print(sum % 3)
    print(sum % 3 == 0)

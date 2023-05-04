def sequence_del(my_str):
    result = ""
    for i in range(len(my_str)):
        if i == 0 or my_str[i] != my_str[i - 1]:
            result += my_str[i]
    return result


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))


if __name__ == '__main__':
    main()

def operation_on_files(path, operation, param=None):
    with open(path, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

        if operation == 'sort':
            words = set(word for line in lines for word in line.split())
            sorted_words = sorted(words)
            print(sorted_words)

        if operation == 'rev':
            reversed_lines = [line[::-1] for line in lines]
            print(reversed_lines)

        if operation == 'last':
            n = int(param)
            last_lines = lines[-n:]
            print(last_lines)


def main():
    operation_on_files("sampleFile.txt", "last", 1)
    operation_on_files("sampleFile.txt", "rev")
    operation_on_files("sampleFile.txt", "sort")


if __name__ == '__main__':
    main()

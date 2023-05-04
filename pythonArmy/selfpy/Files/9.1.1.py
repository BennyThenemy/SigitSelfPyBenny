def are_files_equal(file1, file2):
    open_file1 = open(file1, "r")
    open_file2 = open(file2, "r")

    content1 = open_file1.read()
    content2 = open_file2.read()

    open_file1.close()
    open_file2.close()

    if content1 == content2:
        return True
    return False


def main():
    print(are_files_equal("copy_of_file1.txt", "file1.txt"))


if __name__ == '__main__':
    main()

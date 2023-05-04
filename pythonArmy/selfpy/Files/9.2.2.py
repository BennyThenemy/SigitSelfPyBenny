def copy_file_content(source, destination):
    with open(destination, "w") as des:
        src = open(source, "r")
        des.write(src.read())


def main():
    copy_file_content("copy.txt", "paste.txt")


if __name__ == '__main__':
    main()



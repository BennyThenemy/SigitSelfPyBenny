def who_is_missing(file_path):
    with open(file_path, 'r') as file:
        nums = list(map(int, file.readline().split(",")))

        found_file_msg = ""
        for index in range(1, max(nums) + 1):
            if index not in nums:
                found_file_msg += str(index) + ", "

        if found_file_msg != "":
            with open('found.txt', 'w') as found_file:
                found_file.write(str(found_file_msg))


def main():
    who_is_missing("numbers.txt")


if __name__ == '__main__':
    main()

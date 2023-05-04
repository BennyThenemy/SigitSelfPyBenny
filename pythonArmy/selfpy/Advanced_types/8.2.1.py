def message():
    data = ("self", "py", 1.543)
    format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"

    print(format_string % data)


def main():
    message()


if __name__ == '__main__':
    main()


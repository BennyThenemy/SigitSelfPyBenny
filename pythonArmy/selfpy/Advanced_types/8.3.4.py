def inverse_dict(my_dict):
    new_dict = {}
    for key in my_dict:
        if my_dict[key] in new_dict:
            new_dict[my_dict[key]] = list(new_dict[my_dict[key]])
            new_dict[my_dict[key]].append(key)
        else:
            new_dict[my_dict[key]] = key

    return new_dict


def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))


if __name__ == '__main__':
    main()

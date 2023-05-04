from datetime import datetime


def age(birthdate):
    date_string = "27.03.1970"
    date_format = "%d.%m.%Y"
    dob = datetime.strptime(date_string, date_format)
    today = datetime.today()
    my_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    return my_age


def get_info(given_dict):
    answer = 17
    while answer != -1:
        answer = int(input("What do you wanna know?: "))
        if answer == 1:
            print(given_dict["last_name"])

        elif answer == 2:
            date_string = "27.03.1970"
            date_format = "%d.%m.%Y"
            dob = datetime.strptime(date_string, date_format)
            print(dob.strftime("%m"))

        elif answer == 3:
            print(len(given_dict["hobbies"]))

        elif answer == 4:
            print(given_dict["hobbies"][len(given_dict["hobbies"])-1])

        elif answer == 5:
            given_dict["hobbies"].append("Cooking")

        elif answer == 6:
            date_tuple = tuple(given_dict["birth_date"].split('.'))
            print(date_tuple)

        elif answer == 7:
            given_dict["age"] = age(given_dict["birth_date"])

        else:
            print("Bye Man")

        print(given_dict)


def main():
    my_dict = {"first_name": "Mariah",
               "last_name": "Carey",
               "birth_date": "27.03.1970",
               "hobbies": ["Sing", "Compose", "Act"]}

    get_info(my_dict)


if __name__ == '__main__':
    main()

# for statement 7 in the shopping org function:
special_characters = ["'", '"', "!", "@", "#", "$", "%", "^", "&", "*", "(",
                          ")", "-", "+", "?", "_", "=", "<", ">", "/", ".", ","]


def shopping_org(shopping_string):
    # Converting the shopping_string to shopping_list:
    shopping_list = list(shopping_string.split(","))

    # The options
    print("""
                    1. Printing the list of products
                    2. Printing the number of products in the list
                    3. Printing the answer to the test "Is the product on the list?"
                    4. Printing the answer to the test "How many times does a certain product appear?"
                    5. Deleting a product from the list
                    6. Adding a product to the list
                    7. Printing all invalid products
                    8. Removing all existing duplicates in the list
                    9. Exit
    """)

    answer = 0
    while answer != 9:

        # request answer
        answer = int(input("What would you like to know?: "))

        if answer == 1:
            print(shopping_list)

        elif answer == 2:
            print(len(shopping_list))

        elif answer == 3:
            request = input("enter the item you are looking for: ")
            print(request in shopping_list)

        elif answer == 4:
            request = input("enter the item you are looking for: ")
            print(shopping_list.count(request))

        elif answer == 5:
            request = input("enter the item you want to delete: ")
            if request in shopping_list:
                shopping_list.remove(request)

        elif answer == 6:
            request = input("enter the item you want to add: ")
            shopping_list.append(request)

        elif answer == 7:
            for item in shopping_list:
                if len(item) < 3:
                    print(item)

                else:
                    for char in item:
                        for sign in special_characters:
                            if char == sign:
                                return True

        elif answer == 8:
            shopping_list = list(dict.fromkeys(shopping_list))
        else:
            pass


def main():
    my_shopping_list = "Milk,Cottage,Tomatoes"
    shopping_org(my_shopping_list)


if __name__ == '__main__':
    main()

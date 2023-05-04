import random


def func(num1, num2):
    """
    The function returns funny story using the numbers that given
    :param num1: first number in the story
    :param num2: second number in the story
    :return: string that contains num1 and num2
    """
    random_story = ["I had " + str(num1) + " cakes, I ate " + str(num2) + " of them (:",
                    "I saw in Spain " + str(num1) + " men trying to eat " + str(num2) + " Tacos!",
                    "There is only " + str(num1) + " Benny in the world, and I love him so much so "
                    "I am going to send him " + str(num2) + " in bit"]
    return random.choice(random_story)


def main():
    print(func(1, 300))
    print(func.__doc__)


if __name__ == '__main__':
    main()

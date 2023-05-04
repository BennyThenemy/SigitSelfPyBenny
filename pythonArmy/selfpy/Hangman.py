import random


def pic1():
    print("""\
    x-------x 
    """)


def pic2():
    print("""\
    x-------x
    |
    |
    |
    |
    |
    """)


def pic3():
    print("""\
    x-------x
    |       |
    |       0
    |
    |
    |
    """)


def pic4():
    print("""\
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """)


def pic5():
    print("""\
    x-------x
    |       |
    |       0
    |      /||
    |
    |

    """)


def pic6():
    print("""\
    x-------x
    |       |
    |       0
    |      /||
    |      /
    |
    """)


def pic7():
    print("""\
    x-------x
    |       |
    |       0
    |      /||
    |      / |
    |
    """)


HANGMAN_ASCII_ART = """Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
    """

MAX_TRIES = 7

HANGMAN_PHOTOS = {1: pic1,
                  2: pic2,
                  3: pic3,
                  4: pic4,
                  5: pic5,
                  6: pic6,
                  7: pic7
                  }


def choose_word(file_path, index):
    with open(file_path, 'r') as f:
        words = f.read().split()
        num_words = len(set(words))
        secret_word = words[index % len(words)]
        return num_words, secret_word


def print_hangman(num_of_tries):
    HANGMAN_PHOTOS[num_of_tries]()


def has_signs(my_word):
    """
    :param my_word: letter_guessed
    :return: True - if word contains any of signs, else - False
    """
    # Checks if word contains any of these signs:
    special_characters = ["'", '"', "!", "@", "#", "$", "%", "^", "&", "*", "(",
                          ")", "-", "+", "?", "_", "=", "<", ">", "/", ".", ","]
    for letter in my_word:
        for sign in special_characters:
            if letter == sign:
                return True

    return False


def is_valid_input(letter_guessed, old_letters_guessed):
    """
    checking if the letter is valid
    :param old_letters_guessed: contains the letters that already have been guessed
    :param letter_guessed: the letter that the player guessed
    :return: True: if the length of letter_guessed is 1 or doesn't contain any signs, else - False
    """
    if len(letter_guessed) > 1 and has_signs(letter_guessed):
        # if letter's length is more than 1 and has signs
        print("E3")
    elif len(letter_guessed) > 1:
        # if letter's length is more than 1
        print("E1")
    elif has_signs(letter_guessed):
        # if the letter is a sign
        print("E2")
    else:
        if old_letters_guessed.count(letter_guessed) == 0:
            print(letter_guessed)
            return True

    return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: the letter that the player guessed.=
    :param old_letters_guessed: contains the letters that already have been guessed
    :return: True - if updating was successful, else - False
    """

    if is_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True

    print('X')
    print(" -> ".join(old_letters_guessed))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word: the secret word that the player has to guess
    :param old_letters_guessed: how many letters does the player guessed
    :return: string with the correct letters: b__b__ly
    """
    guessed_correctly = ""
    for char in secret_word:
        if old_letters_guessed.count(char) > 0:
            guessed_correctly += char
        else:
            guessed_correctly += '_'

    return guessed_correctly


def check_win(secret_word, old_letters_guessed):
    return not show_hidden_word(secret_word, old_letters_guessed).__contains__("_")


if __name__ == '__main__':
    old_letters = list()
    current_tries = 1
    # printing ascii art:
    print(HANGMAN_ASCII_ART)

    # choosing file that contains words
    file_path = input("Please insert your file path: ")
    text_index = input("Please insert index: ")
    num_words, secret_word = choose_word(file_path, int(text_index))

    # while player didn't pass the current_tries the game continue
    while not current_tries > MAX_TRIES:

        # check win
        if check_win(secret_word, old_letters):
            break

        # printing hangman
        print_hangman(current_tries)
        print(show_hidden_word(secret_word, old_letters))

        # the player guessing
        guess = input("Guess a letter: ").lower()

        # if the player already guessed / word char repeating
        while not try_update_letter_guessed(guess, old_letters):
            guess = input("Guess a letter: ").lower()

        # checking if the player was wrong
        if not secret_word.__contains__(guess):
            print(":(")
            current_tries += 1

    # After the game ended checking if the player won
    if current_tries < MAX_TRIES:
        print("WON")
    else:
        print("LOSE")


word = input("Enter a word: ")
word = word.replace(" ", "")
word = word.lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("OK")

from collections import defaultdict


def sort_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        sorted_chars = tuple(sorted(word))
        if sorted_chars in anagrams:
            anagrams[sorted_chars].append(word)
        else:
            anagrams[sorted_chars] = [word]

    # Return the values of the dictionary as a list of lists.
    return list(anagrams.values())


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters',
                     'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']

    print(sort_anagrams(list_of_words))


if __name__ == '__main__':
    main()

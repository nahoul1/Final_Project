def remove_first(wrongs):
    """
    Removes first letter of word
    :param wrongs: Incorrectly spelled word
    :return: list of suggestions for word
    """

    # removes first letter from word
    name = wrongs[0:0] + wrongs[1:]

    all_words = {}
    # creates super dictionary
    with open('all_words.txt', encoding='utf8') as f:
        for word in f:
            word = word.strip().lower()
            all_words[word] = word
    names = []

    # if the word is real, return it
    if name in all_words:
        names.append(name)
        if names is None:
            return 'wah'
        elif names is not None:
            return 'names'
    return ''


k = 'forget'
print(remove_first(k))
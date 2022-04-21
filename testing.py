def remove_last(wrongs):
    """

    :param wrongs: Incorrectly spelled word
    :return: list of suggestions for word
    """
    name = wrongs[:-1]
    all_words = {}
    # creates super dictionary
    with open('all_words.txt', encoding='utf8') as f:
        for word in f:
            word = word.strip().lower()
            all_words[word] = word
    names = []
    if name in all_words:
        names.append(name)
    return names


w = 'cherryy'
print(remove_last(w))
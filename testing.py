def single_letters(wrongs):
    """
    Adds duplicate letters
    :param wrongs: Incorrectly spelled word
    :return: list of suggestions for word
    """
    sug = []
    tran = []

    temp = wrongs
    # adds letter
    for i in range(len(temp)):
        new = temp[:i] + temp[i] + temp[i:]
        tran.append(new)

    all_words = {}
    # creates super dictionary
    with open('all_words.txt', encoding='utf8') as f:
        for word in f:
            word = word.strip().lower()
            all_words[word] = word

    for word in tran:
        if word in all_words:
            sug.append(word)

    suggestions = []
    # checks to see if changes are real words and returns list of ones that are
    for i in sug:
        if i not in suggestions:
            suggestions.append(i)
    if suggestions:
        return suggestions
    else:
        return ''


s = 'carot'

print(single_letters(s))

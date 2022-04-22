def single_letters(wrongs):
    """
    Adds duplicate letters
    :param wrongs: Incorrectly spelled word
    :return: list of suggestions for word
    """
    sug = []
    tran = []

    temp = list(wrongs)
    # adds letter
    for i in range(len(temp)-1):
        temp.insert(i-1, temp[i])
        print(temp)
        tran.append(temp)

    attempts = []
    # puts the word back into a list
    for ele in tran:
        attempt = ''
        for x in ele:
            attempt += x
        attempts.append(attempt)

    all_words = {}
    # creates super dictionary
    with open('all_words.txt', encoding='utf8') as f:
        for word in f:
            word = word.strip().lower()
            all_words[word] = word

    suggestions = []
    # checks to see if permutations are real words and returns list of ones that are
    for i in sug:
        if i not in suggestions:
            suggestions.append(i)
    if suggestions:
        print(suggestions)
    else:
        return ''


k = 'adress'
single_letters(k)

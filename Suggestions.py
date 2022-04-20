from itertools import permutations


class Suggest:

    @staticmethod
    def sing_transposition(wrongs):
        """
        Checks for single transpositions of incorrectly spelled words that are real words
        :param wrongs: List of incorrectly spelled words
        :return: List of suggestions the words can be
        """
        sug = []
        tran = []

        # turns each word into a list of its letters
        perm = permutations(wrongs)  # all permutations of current incorrectly spelled word
        for i in list(perm):
            tran.append(i)  # puts all permuted lists of letters into one list
        attempts = []

        # turns each list of letters into a string
        for ele in tran:
            attempt = ''
            for x in ele:
                attempt += x
            attempts.append(attempt)
        # creates dictionary of every word
        all_words = {}
        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                all_words[word] = word
        # puts all the strings into a list
        for word in attempts:
            if word in all_words:
                sug.append(word)
        suggestions = []
        # checks to see if permutations are real words and returns list of ones that are
        for i in sug:
            if i not in suggestions:
                suggestions.append(i)
        if suggestions:
            return suggestions
        else:
            return ''

    @staticmethod
    def double_letters(wrongs):
        """
        Checks for double letters in incorrectly spelled words to see if that was the mistake
        :param wrongs: Incorrectly spelled words
        :return: List of suggestions words can be
        """
        sug = []
        tran = []

        temp = list(wrongs)
        for i in range(len(temp) - 1):
            if temp[i] == temp[i - 1]:
                del temp[i]
        tran.append(temp)
        attempts = []
        for ele in tran:
            attempt = ''
            for x in ele:
                attempt += x
            attempts.append(attempt)
        all_words = {}
        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                all_words[word] = word
        for word in attempts:
            if word in all_words:
                sug.append(word)
        suggestions = []
        # checks to see if permutations are real words and returns list of ones that are
        for i in sug:
            if i not in suggestions:
                suggestions.append(i)
        if suggestions:
            return suggestions
        else:
            return ''

    @staticmethod
    def fix(file, word, right, ind):
        """
        Fixes and eventually outputs the modified original text file.
        :param file: original textfile
        :param word: originally misspelled word
        :param right: the array of options
        :param ind: the index of the word
        :return: modified text file
        """
        f = open(file, "r+")
        l = f.readlines()
        for i in range(len(right)):
            if ind == i:
                fix = right[i]
        for ele in l:
            if word in ele:
                replacement = ele.replace(word, fix)
                l = replacement
        f.truncate(0)
        f.seek(0)
        f.writelines(l)

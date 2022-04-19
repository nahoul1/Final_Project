from itertools import permutations


class Suggest:

    def __init__(self, all_words):
        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                all_words[word] = word
        self.all_words = {}

    @staticmethod
    def sing_transposition(wrongs):
        """
        Checks for single transpositions of incorrectly spelled words that are real words
        :param wrongs: List of incorrectly spelled words
        :return: List of suggestions the words can be
        """
        sug = []
        trans = []

        # turns each word into a list of its letters
        for ele in wrongs:
            res = ele[:]
            temp = list(res)
            perm = permutations(temp)
            for i in list(perm):
                trans.append(i)  # puts all permuted lists of letters into one list
        attempts = []

        # turns each list of letters into a string
        for ele in trans:
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
        return suggestions

    @staticmethod
    def double_letters(wrongs):
        """
        Checks for double letters in incorrectly spelled words to see if that was the mistake
        :param wrongs: Incorrectly spelled words
        :return: List of suggestions words can be
        """

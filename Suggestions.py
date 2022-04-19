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
        for ele in wrongs:
            res = ele[:]
            temp = list(res)
            perm = permutations(temp)  # all permutations of current incorrectly spelled word
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
        return suggestions

    @staticmethod
    def double_letters(wrongs):
        """
        Checks for double letters in incorrectly spelled words to see if that was the mistake
        :param wrongs: Incorrectly spelled words
        :return: List of suggestions words can be
        """
        sug = []
        tran = []
        for ele in wrongs:
            res = ele[:]
            temp = list(res)
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
        return suggestions

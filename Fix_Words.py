from itertools import permutations


class Modify:

    def __init__(self, new_f):
        self.new_f = new_f

    @staticmethod
    def remove_punc(words):
        for i in '.,;:"/?()[]{}<>-_!':
            words = words.replace(i, "")
        return words


class Suggest:

    @staticmethod
    def sing_transposition(wrongs):
        sug = []
        trans = []
        for ele in wrongs:
            res = ele[:]
            temp = list(res)
            perm = permutations(temp)
            for i in list(perm):
                trans.append(i)
        attempts = []
        for ele in trans:
            attempt = ''
            for x in ele:
                attempt += x
            attempts.append(attempt)
        k = {}
        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                k[word] = word
        for word in attempts:
            if word in k:
                sug.append(word)
        suggestions = []
        for i in sug:
            if i not in suggestions:
                suggestions.append(i)
        return suggestions


"""
    @staticmethod
    def double_letters(wrongs):
"""

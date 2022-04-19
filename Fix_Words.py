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
        for ele in wrongs:
            temp = list(ele)
            trans = []
            for i in temp:
                res = ele[:]
                ele[i], ele[i-1] = ele[i-1], ele[i]
                trans.append(res)
        k = {}
        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                k[word] = word
        for ele in trans:
            if trans[ele] in k:
                sug.append(trans[ele])
        return sug




"""
    @staticmethod
    def double_letters(wrongs):
"""

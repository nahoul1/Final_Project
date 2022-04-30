from itertools import permutations


class Suggest:

    def __init__(self, wrongs, all_words):
        self.wrongs = wrongs
        self.all_words = all_words

    def transposition(self):
        """
        Checks for all transpositions of incorrectly spelled words that are real words
        :return: List of suggestions the word can be
        """
        sug = []
        tran = []

        # turns each word into a list of its letters
        perm = permutations(self.wrongs)  # all permutations of current incorrectly spelled word
        for i in list(perm):
            tran.append(i)  # puts all permuted lists of letters into one list
        attempts = []

        # turns each list of letters into a string
        for ele in tran:
            attempt = ''
            for x in ele:
                attempt += x
            attempts.append(attempt)

        # puts all the strings into a list
        for word in attempts:
            if word in self.all_words:
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

    def double_letters(self):
        """
        Checks for double letters in incorrectly spelled words to see if that was the mistake
        :return: List of suggestions words can be
        """
        sug = []
        tran = []

        # deletes double consecutive occurrences of a letter in a word
        crate = self.wrongs
        temp = list(crate)
        for i in range(len(temp) - 1):
            if temp[i] == temp[i - 1]:
                del temp[i]
        tran.append(temp)

        attempts = []
        # puts the word back into a list
        for ele in tran:
            attempt = ''
            for x in ele:
                attempt += x
            attempts.append(attempt)

        # checks if word is real
        for word in attempts:
            if word in self.all_words:
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

    def single_letters(self):
        """
        Adds duplicate letters
        :return: list of suggestions for word
        """
        sug = []
        tran = []

        temp = self.wrongs
        # adds letter
        for i in range(len(temp)):
            new = temp[:i] + temp[i] + temp[i:]
            tran.append(new)

        # checks if word is real
        for word in tran:
            if word in self.all_words:
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

    def remove_first(self):
        """
        Removes first letter of word
        :return: list of suggestions for word
        """

        # removes first letter from word
        name = self.wrongs[0:0] + self.wrongs[1:]
        names = []

        # if the word is real, return it
        if name in self.all_words:
            names.append(name)
            if names:
                return names
            else:
                return ''
        return ''

    def remove_last(self):
        """
        Removes last letter of word
        :return: list of suggestions for word
        """
        # removes last letter from word
        name = self.wrongs[:-1]
        names = []

        # if the word is real, return it
        if name in self.all_words:
            names.append(name)
        if names:
            return names
        else:
            return ''


class Fix:

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
        # opens the file and finds the incorrect word
        if right[ind] == 'Not an option':
            return
        f = open(file, "r+")
        l = f.readlines()
        for i in range(len(right)):
            if ind == i:
                corr = right[i]

        # replace incorrect word with correct word
        for ele in l:
            if word in ele:
                replacement = ele.replace(word, corr)
                l = replacement

        # fix the text file
        f.truncate(0)
        f.seek(0)
        f.writelines(l)

from Suggestions import Suggest
from Suggestions import Fix


class Behold:
    """Shows Textfile"""
    def __init__(self, file):
        self.file = file

    def original(self):
        """
        Shows contents of text file
        :return: The text file
        """
        with open(self.file, encoding='utf8') as t:
            new = t.read()
        print(new)
        return ''


class Modify:

    def __init__(self, file):
        self.file = file

    @staticmethod
    def remove_punc(words):
        """
        Removes all punctuation from the textfile so words can
        be crosschecked with dictionary
        :param words: words in the text file
        :return:The words without any punctuation
        """
        for i in '.,;:"/?()[]{}<>-_!':
            words = words.replace(i, "")
        return words

    def check(self):
        """
        Detects incorrectly spelled words and offers suggestions
        :return: All the incorrect words and suggestions
        """

        all_words = {}
        # creates super dictionary
        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                all_words[word] = word

        # opens file and removes punctuation and makes all characters lower
        with open(self.file, encoding='utf8') as t:
            new = t.read()
        new = Modify.remove_punc(new).lower().strip()
        new = new.split()

        wrong = []
        # creates a list of incorrect words
        for word in new:
            if word not in all_words:
                wrong.append(word)
        # traverses list and gives suggestions
        for word in wrong:
            lexicon = Suggest(word, all_words)  # creates object
            print(word, "is spelled incorrectly, did you mean:")
            p = Suggest.transposition(lexicon)  # suggestions using permutation method
            k = Suggest.double_letters(lexicon)  # suggestions using double method
            j = Suggest.remove_last(lexicon)  # suggestions removing the last letter
            v = Suggest.remove_first(lexicon)  # suggestions removing the first letter
            c = Suggest.single_letters(lexicon)  # suggestions doubling each letter
            w = [*p, *k, *j, *v, *c, 'Not an option']

            print(w)
            n = int(input("Enter the number of the correct word's place: "))
            while n > (len(w) - 1):
                print("Invalid entry. Try again.")
                n = int(input("Enter the number of the correct word's place: "))
            Fix.fix(self.file, word, w, n-1)  # fixes the original text file
        print("The corrected text is:")
        f = Behold(self.file)
        print(Behold.original(f))
        return ''

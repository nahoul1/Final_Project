from Suggestions import Suggest
from Suggestions import Fix


class Modify:

    @staticmethod
    def original(file):
        with open(file, encoding='utf8') as t:
            new = t.read()
        print(new)

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

    @staticmethod
    def check(file):
        """
        Detects incorrectly spelled words and offers suggestions
        :param file: Text file with words that will be checked
        :return: All the incorrect words and suggestions
        """

        all_words = {}
        # creates super dictionary
        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                all_words[word] = word

        # opens file and removes punctuation and makes all characters lower
        with open(file, encoding='utf8') as t:
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
            print(word, "is spelled incorrectly, did you mean:")
            p = Suggest.transposition(word)  # suggestions using permutation method
            k = Suggest.double_letters(word)  # suggestions using double method
            j = Suggest.remove_last(word)  # suggestions removing the last letter
            v = Suggest.remove_first(word)
            c = Suggest.single_letters(word)
            w = [*p, *k, *j, *v, *c, 'Not an option']
            print(w)
            n = int(input("Enter the number of the correct word's place: "))
            Fix.fix(file, word, w, n-1)  # fixes the original text file
        print("The corrected text is:")
        print(Modify.original(file))
        return ''

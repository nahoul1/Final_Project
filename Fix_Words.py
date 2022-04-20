from Suggestions import Suggest


class Modify:

    @staticmethod
    def original(file):
        with open(file, encoding='utf8') as t:
            new = t.read()
        print(new)

    @staticmethod
    def remove_punc(words):
        """
        Removes all punctuation from the textfile so words can be crosschecked with dictionary
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

        with open('all_words.txt', encoding='utf8') as f:
            for word in f:
                word = word.strip().lower()
                all_words[word] = word

        with open(file, encoding='utf8') as t:
            new = t.read()
        new = Modify.remove_punc(new)
        new = new.split()
        wrong = []
        for word in new:
            if word not in all_words:
                wrong.append(word)
        for word in wrong:
            print(word, "is spelled incorrectly, did you mean:")
            p = Suggest.sing_transposition(word)
            k = Suggest.double_letters(word)
            w = [*p, *k]
            print(w)
            n = int(input("Enter the number of the correct word's place: "))
            Suggest.fix(file, word, w, n-1)
        print("The corrected text is:")
        print(Modify.original(file))

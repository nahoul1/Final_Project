from Suggestions import Suggest


class Modify:

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
        print("The word(s)", wrong, "are spelled incorrectly.\n Did you mean:")
        print(Suggest.sing_transposition(wrong))


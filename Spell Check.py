
from Fix_Words import Modify, Suggest
# create dictionary with every word and cross-check words with

all_words = {}

with open('all_words.txt', encoding='utf8') as f:
    for word in f:
        word = word.strip().lower()
        all_words[word] = word


with open('tests.txt', encoding='utf8') as t:
    new = t.read()

wrong = []
new = Modify.remove_punc(new)
new = new.split()


for word in new:
    if word not in all_words:
        wrong.append(word)

print("The word(s)", wrong, "are spelled incorrectly.\n Did you mean:")
print(Suggest.sing_transposition(wrong))

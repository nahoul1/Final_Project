
from Fix_Words import Modify
# create dictionary with every word and cross-check words with

all_words = {}

with open('all_words.txt', encoding='utf8') as f:
    for word in f:
        word = word.strip().lower()
        all_words[word] = word


with open('tests.txt', encoding='utf8') as t:
    for word in t:
        new = word.strip().lower().split()

wrong = []
for word in new:
    if word not in all_words:
        wrong.append(word)


from nltk import word_tokenize, pos_tag, download
import os
from sklearn.feature_extraction.text import TfidfVectorizer

download('punkt')
download('averaged_perceptron_tagger')
with open('../pride.txt') as pride:
    text = pride.read()

tokens = word_tokenize(text)
tags = pos_tag(tokens)
proper_nouns = []
for tag in tags:
    if tag[1] == 'NNP':
        proper_nouns.append(tag[0])
print(set(proper_nouns))

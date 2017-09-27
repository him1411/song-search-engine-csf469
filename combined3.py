from math import log
import nltk
from nltk import word_tokenize
import sys
import optparse
import logging
import os
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
from os import walk

vocabulary = {}
document_tokens_list[]
docFiles = [f for f in os.listdir('.') if os.path.isfile(f)]

def __build_vocabulary(document_tokens):
        vocabulary_index=len(vocabulary)-1
            for word in document_tokens:
                if word not in vocabulary:
                            vocabulary[word] = vocabulary_index
                            vocabulary_index+= 1

document_tokens1 = [word for sent in nltk.sent_tokenize((getText("HP1.txt")).decode('utf-8')) for word in nltk.word_tokenize(sent)]
document_tokens1 = [stemmer.stem(t) for t in document_tokens1]
document_tokens1 = [stemmer.stem(t) for t in document_tokens1 if t not in nltk.corpus.stopwords.words('english')]
document_tokens_list=[document_tokens1]

for file in list:
    file_name="./Documents/"+file
    __build_vocabulary(file_name)

for document_tokens in document_tokens_list:
    __build_vocabulary(document_tokens)
print (vocabulary)

j=0
primaryDictionary = dict()
print (len(document_tokens_list))

for vocab in vocabulary:
    j+=1
    if vocab not in primaryDictionary:
        inner_dict=dict()
        for i in range(len(document_tokens_list)):
            inner_dict[i]=dict()
            inner_dict[i]=(tf_idf_rapport(vocab,document_tokens_list[i],document_tokens_list))
    primaryDictionary[vocab]=inner_dict

print (primaryDictionary)

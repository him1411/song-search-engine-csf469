from math import log
import nltk
from nltk import word_tokenize
from nltk import FreqDist
import sys
import math
import os
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import json

vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list= []
temp_doc_tokens = []
snowball_stemmer = SnowballStemmer('english')
docFiles = [f for f in os.listdir('./chota_corpus') if f.endswith(".html")]

def __build_vocabulary(document_tokens):
        vocabulary_index=len(vocabulary)-1
        for word in document_tokens:
            if word not in vocabulary_idf:
                vocabulary_idf[word] = 1
                print(vocabulary_index)
            else:
                vocabulary_idf[word] = vocabulary_idf[word] + 1

            if word not in vocabulary:
                        vocabulary[word] = vocabulary_index
                        vocabulary_index+= 1

def buildIDF():
    for word in vocabulary:
        for document_tokens in document_tokens_list:
            if word in document_tokens:
                if word in vocabulary_idf:
                    vocabulary_idf[word] = vocabulary_idf[word] + 1
                else:
                    vocabulary_idf[word] = 1

def buildFreqDist(document_tokens_list):
    i=0
    for document_tokens in document_tokens_list:
        freqDist[i] = FreqDist(document_tokens)
        i = i + 1
        for word in document_tokens:
            vocabulary_idf

def returnTermFrequency(term, document_tokens, document_tokens_index):
    return math.log2(1+(freqDist[document_tokens_index][term]/float(len(document_tokens))))

def returnIdf(term):
    return math.log2(len(document_tokens_list)/vocabulary_idf[term])

#****************************************************************************************************************************#
count=0
for file in docFiles:
    #print(file)
    file_name = open("./chota_corpus/"+file)
    print(count)
    count+=1
    words = file_name.read()
    temp_doc_tokens = nltk.word_tokenize(words)
    temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
    temp_doc_tokens = [snowball_stemmer.stem(token) for token in temp_doc_tokens]
    temp_doc_tokens = [snowball_stemmer.stem(token) for token in temp_doc_tokens if token not in nltk.corpus.stopwords.words('english')]
    document_tokens_list.append(temp_doc_tokens)
    #print(temp_doc_tokens[:20])

#print(document_tokens_list)
for document_tokens in document_tokens_list:
    __build_vocabulary(document_tokens)

print (len(vocabulary) )

with open('./savers/chota.json', 'w') as fp:
    json.dump(vocabulary, fp)

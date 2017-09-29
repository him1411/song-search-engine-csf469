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

vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list= []
temp_doc_tokens = []
snowball_stemmer = SnowballStemmer('english')
docFiles = [f for f in os.listdir('./Documents') if f.endswith(".txt")]

def __build_vocabulary(document_tokens):
        vocabulary_index=len(vocabulary)-1
        for word in document_tokens:
                if word not in vocabulary_idf:
                    vocabulary_idf[word] = 1
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

for file in docFiles:
    print(file)
    file_name = open("./Documents/"+file)
    words = file_name.read()
    temp_doc_tokens = nltk.word_tokenize(words)
    temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
    temp_doc_tokens = [snowball_stemmer.stem(token) for token in temp_doc_tokens]
    temp_doc_tokens = [snowball_stemmer.stem(token) for token in temp_doc_tokens if token not in nltk.corpus.stopwords.words('english')]
    document_tokens_list.append(temp_doc_tokens)
    print(temp_doc_tokens[:20])

for document_tokens in document_tokens_list:
    __build_vocabulary(document_tokens)
print (vocabulary)
buildFreqDist(document_tokens_list)
buildIDF()
print(vocabulary_idf)
j=0
k=0;
primaryDictionary = dict()

for vocab in vocabulary:
    j+=1
    if vocab not in primaryDictionary:
        inner_dict=dict()
        k=0
        for document_tokens in document_tokens_list:
            inner_dict[k]=dict()
            termFreq = returnTermFrequency(vocab, document_tokens, k)
            idf = returnIdf(vocab)
            inner_dict[k] = {1:termFreq,2:idf,3:(termFreq*idf)}
            k = k + 1
            #inner_dict[i]=(tf_idf_rapport(vocab,document_tokens_list[i],document_tokens_list))
    primaryDictionary[vocab]=inner_dict
#print (primaryDictionary)

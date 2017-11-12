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
import  json

vocabulary = {}
vocabulary_idf = {}
freqDist = {}
document_tokens_list= []
temp_doc_tokens = []
snowball_stemmer = SnowballStemmer('english')
docFiles = [f for f in os.listdir('./corpus') if f.endswith(".txt")]
docFiles.sort()


def compute_vocabulary():
    """
    Function for retreiving the document_tokens_list for creating the vocabulary,then storing the vocabulary in a json file
    """
    with open('./savers/document_tokens_list.json') as json_data:
        document_tokens_list = json.load(json_data)

    for document_tokens in document_tokens_list:
        __build_vocabulary(document_tokens)
        
    with open('savers/vocabulary.json', 'w') as fp:
        json.dump(vocabulary, fp)

def __build_vocabulary(document_tokens):
        """
        Function for building the vocabulary i.e. the dictionary which has all the unique words in the corpus
        """
        count=0

        vocabulary_index=len(vocabulary)-1
        for word in document_tokens: # accsessing words in document tokens list
                if word not in vocabulary:
                            print(count)
                            count+=1
                            vocabulary[word] = vocabulary_index
                            vocabulary_index+= 1


compute_vocabulary()



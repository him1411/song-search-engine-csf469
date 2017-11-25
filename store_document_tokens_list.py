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


for i in range(len(docFiles)):
    docFiles[i] = int(docFiles[i].split(".")[0])
    print(docFiles[i])

docFiles.sort()
print(docFiles)

def create_document_tokens_list():
    """
    Function for creating document_tokens_list and then storing in json file for further usage
    """
    count=0
    for file in docFiles:
        file_name = open("./corpus/"+ str(file) + ".txt")
        print(count)
        count+=1
        words = file_name.read()
        temp_doc_tokens = nltk.word_tokenize(words)
        temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
        #temp_doc_tokens = [snowball_stemmer.stem(token) for token in temp_doc_tokens]
        temp_doc_tokens = [token for token in temp_doc_tokens if token not in nltk.corpus.stopwords.words('english')]
        document_tokens_list.append(temp_doc_tokens)


    #storing in json file
    with open('savers/document_tokens_list.json', 'w') as fp:
        json.dump(document_tokens_list, fp)


#caling function
create_document_tokens_list()

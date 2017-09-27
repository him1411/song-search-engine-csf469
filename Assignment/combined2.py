from math import log
from nltk import word_tokenize
import sys
import optparse
import logging
import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.sparsetools as sptools
import collections
from collections import defaultdict
import pickle
import json

vocabulary = {}
from os import walk
list = os.listdir("./list_of_documents")
smoothing = 1
ft_matrix = []
ifd_diag_matrix = []
tf_idf_matrix = []

def __build_vocabulary(location):
        #will have to work on preprocessing ,etc here itself or make calls to the same
        """Build vocabulary with indexable objects.

        Args:
          objects (list of Indexable): Indexed objects that will be
            considered during ranking.

        """
        vocabulary_index=len(vocabulary)
        with open(location, 'r') as f:
            words=f.read()
            word_s=words.split()
            for word in word_s:
                if word not in vocabulary:
                            vocabulary[word] = vocabulary_index
                            vocabulary_index+= 1

#function for finding the count_for_word in document
def count_for_word(file,word):
    with open("./list_of_documents/"+file, 'r') as f:
            words=f.read()
            count=words.count(words)
            #print count
    return count


# Returns list of word tokens for a string
# Simple tokenizer for illustration purposes only
# Check out NLTK.word_tokenize()
def simple_tokenizer(document):
	return document.lower().split(None)

# Returns integer Term Count for a document
# tc = count number of term occurence in document
def term_count(term, document_tokens):
	return document_tokens.count(term.lower())

# Returns integer with total number of tokens in a document
# toc = count number of tokens in a document
def token_count(document_tokens):
	return len(document_tokens)

# Returns float term frequency (TF),
# normalized for document size
# tf = term count / token count
def term_frequency(term, document_tokens):
	return term_count(term, document_tokens) / float(token_count(document_tokens))

# Returns the number of documents containing the term
# from a list of document tokens
def nr_docs_with_term(term, document_tokens_list):
	nr = 0
	for document_tokens in document_tokens_list:
		if term_count(term, document_tokens) > 0:
			nr += 1
	return nr

# Returns the float Inverse Document Frequency  (IDF)
# normalized to reduce non-unique/common words that appear in many documents
def inverse_document_frequency(term, document_tokens_list):
	return len(document_tokens_list) / 1+float(nr_docs_with_term(term, document_tokens_list))

# Returns the float Term Frequency - Inverse Document Frequency or tf-idf
def tf_idf(term, document_tokens, document_tokens_list):
	return term_frequency(term, document_tokens) * inverse_document_frequency(term, document_tokens_list)

# prints a rapport of all related values
def tf_idf_rapport(term, document_tokens, document_tokens_list):

	#print "Term:", term
	#print "Number of documents:", len(document_tokens_list)
	#print "First 5 document tokens:", document_tokens[:5]
	#print "Term count in document", term_count(term, document_tokens)
	#print "Token count in document:", token_count(document_tokens)
	#print "Number of documents with term:", nr_docs_with_term(term, document_tokens_list)
	#print "TF:\t\t", term_frequency(term, document_tokens)
	#print "IDF:\t\t", inverse_document_frequency(term, document_tokens_list)
	#print "TF--IDF:\t",tf_idf(term, document_tokens, document_tokens_list)
    combined_List=dict()
    combined_List={1:term_count(term, document_tokens),2:token_count(document_tokens),3: nr_docs_with_term(term, document_tokens_list),4:term_frequency(term, document_tokens),5: inverse_document_frequency(term, document_tokens_list),6:tf_idf(term, document_tokens, document_tokens_list)}
    return (combined_List)

def getText(doc_name):
    data=""
    with open (doc_name, "r") as myfile:
        data=myfile.read()
    return data

# Simple sample usage
term = "obnoxious"
dir="./smaller_list_of_documents1/"
document_tokens1 = simple_tokenizer(getText(dir+"HP1.txt"))
document_tokens2 = simple_tokenizer(getText(dir+"HP2.txt"))
#document_tokens3 = simple_tokenizer(getText(dir+"HP3.txt"))
##document_tokens4 = simple_tokenizer(getText(dir+"HP4.txt"))
##document_tokens5 = simple_tokenizer(getText(dir+"HP5.txt"))
#document_tokens6 = simple_tokenizer(getText(dir+"HP6.txt"))
#document_tokens7 = simple_tokenizer(getText(dir+"HP7.txt"))
#document_tokens_list = [document_tokens1, document_tokens2, document_tokens3,document_tokens4,document_tokens5,document_tokens6,document_tokens7]
document_tokens_list=[document_tokens1,document_tokens2]

#for item in document_tokens_list:
#	tf_idf_rapport(term, item, document_tokens_list)
#print document_tokens1

for file in list:
    file_name="./list_of_documents/"+file
    __build_vocabulary(file_name)

print (vocabulary)
list.sort()

megadict = dict()

count=0
j=0
print (len(document_tokens_list))
for vocab in vocabulary:
    j+=1
    print (j)
    if vocab not in megadict:
        inner_dict=dict()
        for i in range(len(document_tokens_list)):

        #inner_dict[item]=tf_idf_rapport(vocab,item,document_tokens_list)
            #print ((words))
            inner_dict[i]=dict()
            inner_dict[i]=(tf_idf_rapport(vocab,document_tokens_list[i],document_tokens_list))

        ## inner_dict[item]=(type(tf_idf_rapport(vocab,item,document_tokens_list)))
    megadict[vocab]=inner_dict


print (megadict)

#f = open('savers/pickletry.p', 'w')   # Pickle file is newly created where foo1.py is
#pickle.dump(megadict, f)          # dump data to f
#f.close()

json = json.dumps(megadict)
f = open("./savers/dict.json","w")
f.write(json)
f.close()
"""print vocabulary
    for vocab in vocabulary:
    print type(tf_idf_rapport(vocab,document_tokens1,document_tokens_list))"""

"""for vocab in vocabulary:
    if  vocab not in megadict:
        inner_dict=dict()
        #inner_dict=collections.defaultdict(list)
        #print count
        #count+=1
        for item in document_tokens_list:
           #combinedList =  tf_idf_rapport(vocab,item,document_tokens_list)
            #inner_dict[item]=list()
            inner_dict[item]=tf_idf_rapport(vocab,item,document_tokens_list)
           #lst = lambda :combinedList
           #for i in range(len(combinedList)):
            #inner_dict[item].append(combinedList[i])
           #inner_dict= defaultdict(lst)
           # inner_dict[item].append(tf_idf_rapport(vocab,item,document_tokens_list))
        megadict[vocab]=inner_dict

print (megadict)"""



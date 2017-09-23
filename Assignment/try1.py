import sys
import optparse
import logging
import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.sparsetools as sptools
#vocabulary (dict): Dictionary containing unique words of the corpus as
#        keys and their respective global index used in tf-idf data structures.

vocabulary = {}
from os import walk
list = os.listdir("./list_of_documents")
smoothing = 1
ft_matrix = []
ifd_diag_matrix = []
tf_idf_matrix = []

#global vocabulary_index
#vocabulary_index=0

def __build_vocabulary(location):
        #will have to work on preprocessing ,etc here itself or make calls to the same
        """Build vocabulary with indexable objects.

        Args:
          objects (list of Indexable): Indexed objects that will be
            considered during ranking.

        """
        vocabulary_index=len(vocabulary)-1
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
            print count
    return count


#function for building rank
def build_rank():
    n_terms = len(vocabulary)
    n_docs = len(list)
    #ft_matrix = sp.lil_matrix((n_docs, n_terms), dtype=np.dtype(float))
    ft_matrix=np.zeros((7,600000),dtype=(float))
    count=1
    for index,indexable in enumerate(list):
        for index, indexable in enumerate(list):
            for key,value in vocabulary.iteritems():
                #word_index_in_vocabulary = self.vocabulary[word]
                doc_word_count = count_for_word(indexable,key)
                ft_matrix[index, value] = doc_word_count
        #ft_matrix = ft_matrix.tocsc()

        print ft_matrix

#we can't guarantee the order in which the files will be walked

#function for beginning to execute search
def execute_search():
    query = None
    while query is not '':
        query = raw_input('Enter a query, or hit enter to quit: ')
        print query




#class for tf-idf



#############################################################

for file in list:
    file_name="./list_of_documents/"+file
    __build_vocabulary(file_name)

print vocabulary
list.sort()
execute_search()
build_rank()





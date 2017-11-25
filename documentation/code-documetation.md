# Code Documentation
the files for which the documentation is being done are :
1. store_document_tokens_list.py
2. store_vocabulary.py
3. store_megadict.py
4. store_scores_gui.py

## Modules/ libraries which were imported
-
-


## store_document_tokens_list.py


### create_document_tokens_list(): 
- Function for creating document_tokens_list and then storing in json file for further usage and then function is being called.
    - Data taken from : /corpus/x.txt  where x is the file number
    - Data stored in : savers/document_tokens_list.json




## store_vocabulary.py
- compute_vocabulary() is called which in turn accesses __build_vocabulary() function to build the vocabulary. The descriptions of the functions are given below :


### compute_vocabulary():
 - Function for retreiving the document_tokens_list for creating the vocabulary,then storing the vocabulary in a json file
     - Data taken from : ./savers/document_tokens_list.json
     - functions called : __build_vocabulary(document_tokens)
     - Data stored in : savers/vocabulary.json


###  __build_vocabulary()
 - Function for building the vocabulary i.e. the dictionary which has all the unique words in the corpus
    -  Parameters given: Document tokens




## store_megadict.py
The code for computing the primary dictionary necessary for tf-idf calculations
The structure is as follows:
It has nested dictionaries which are shown as follows:
- DICTIONARY1-word in vocabulary
    - DICTIONARY2-document_number:
        -  DICTIONARY3- TF,IDF,TF-IDF

- Data accessed from : 
    -  savers/document_tokens_list.json
    -  savers/vocabulary.json
The descriptions of the functions are given below :


### buildIDF()
- function for building the vocabulary IDF from document token list
    - Data accessed from : document_tokens_list
    - Data stored in: vocabulary_idf


### buildFreqDist()
- function for building the FreqDistribution.
    -  Data accessed from : document_tokens_list
    -  Data stored in: freqDist


### returnTermFrequency()
- Function to return the term frequency to main driver code of the file. 
    - parameters : term, document_tokens, document_tokens_index


### returnIdf()
- Function to return corresponding idf by searching in the vocabulary to main driver code of the file. 
    - parameters : term


## store_scores_gui.py
- The main Driver code for
    -  Data accessed from : /corpus/x.txt  where x is the file number, songname.txt
    -  Data stored in: docList


### terminal_function()
-  Function for inputting query and performing query based operations and finally calculating cosine scores. It performs the following features:
    1. Applying stemming porting on queryf documents that a term 't' occurs in and N is the total number of documents in the collection.
    2. calculating frequency
    3. Getting total Document frequency of the word. We have to sum over multiple documents
    4. initializing all documentNormalizedDenominator to zero
    5. for every word in query_wt we parse all documents
    6. The search has been provided with multilingual search support, using google Translate API

    - Data accessed from :
        - savers/document_tokens_list.json
        - savers/vocabulary.json
        - savers/primeDictionary.json 
    - functions called:
        - __build_vocabulary()
        - buildIDF()
        - buildFreqDist
        - returnTermFrequency()
        - returnIdf()
    - Data returned to :
        - savers/store.json
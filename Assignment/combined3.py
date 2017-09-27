import nltk
import json
import math

nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
word_lemmatizer = WordNetLemmatizer()
import unicodedata
import re, math
lookUpTable = {}
corpusSize=2
queryStr = input("Enter a query ").lower()
if(queryStr[0] == "\"" and queryStr[len(queryStr) - 1] == "\""):
    exactMatch = True
queryStr = re.sub("[^A-Za-z0-9 ]+"," ",queryStr)

queryStr = queryStr.strip().split()
queryList=[]
for str in queryStr:
    queryList.append(str)

#getting an entire list of the of elements in the list
#print (queryList)

#retrieving the megadict
megadict={}
"""f = open("./savers/dict.json","rb")
json = f.read()
megadict=json.load(json)
print (megadict)"""
with open('./savers/dict.json') as json_data:
    megadict = json.load(json_data)



###################################################################3
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
	#print "Number of documents with term:", nr_docs_with_term(term, document_tokens_list) #df
	#print "TF:\t\t", term_frequency(term, document_tokens)
	#print "IDF:\t\t", inverse_document_frequency(term, document_tokens_list)
	#print "TF--IDF:\t",tf_idf(term, document_tokens, document_tokens_list)
    combined_List=dict()
    combined_List={1:term_count(term, document_tokens),2:token_count(document_tokens),3: nr_docs_with_term(term, document_tokens_list),4:term_frequency(term, document_tokens),5: inverse_document_frequency(term, document_tokens_list),6:tf_idf(term, document_tokens, document_tokens_list)}
    return (combined_List)
###########################################################

queryDict={} #contains frequency till here i.e the tf
#calculating frequency
for q in queryList:
    if q not in queryDict:
        queryDict[q]=0
    queryDict[q]+=1

#print (queryDict)

queryDf={}
#Getting total Document frequency of the word
for qkey,qvalue in queryDict.items():
    if qkey in megadict:#now here we have one document , we have to sum over multiple documents
        innerDict = megadict[qkey]
        total_frequency_of_documents=0
        #for i in innerDict:
            #total_frequency_of_documents+=innerDict[i]['3']
        #code for getting the total_frequency (sum of all occurence in all documents)
        for i in innerDict:
            if(innerDict[i]['3']>0):
                total_frequency_of_documents+=1
        queryDf[qkey]=total_frequency_of_documents
    else:
        queryDf[qkey]=0

print (queryDf)

queryIdf={}
#check all formulae here
for q in queryDf:
    if (queryDf[q]!=0):
        queryIdf[q] = 1+math.log((corpusSize/queryDf[q]),10)
    else:
         queryIdf[q] = 1+math.log((corpusSize/1+queryDf[q]),10)

print (queryIdf)


#tfWeighting - multiplying tf-raw i.e. tf and Idf

queryWt={}
for q in queryIdf:
    queryWt[q]=queryIdf[q]* queryDict[q]

print (queryWt)

queryNormalizedDenomator=0
for q in queryWt:
    queryNormalizedDenomator+=queryWt[q]*queryWt[q]

print (queryNormalizedDenomator)
queryNormalizedDenomator=(queryNormalizedDenomator)**0.5

queryNormalized={}
for q in queryWt:
    queryNormalized[q] = queryWt[q]/queryNormalizedDenomator

print (queryNormalized)


#Now we need to find the DocumentNormalizedDenominator
documentNormalizedDenominator={}
score = {}
#initializing all documentNormalizedDenominator to zero
for q in megadict:
    innerDict=megadict[q]
    #print(q)
    for i in innerDict:
        documentNormalizedDenominator[i]=0
        score[i]=0

for q in megadict:
    innerDict=megadict[q]
    #print(q)
    for i in innerDict:
    #print (innerDict)
        #print (type(i))
        #documentNormalizedDenominator[i]+=math.pow(innerDict[i][6],2)
        documentNormalizedDenominator[i]+=(math.pow(innerDict[i]['6'],2))
    #documentNormalizedDenominator

for d in documentNormalizedDenominator:
    #print (documentNormalizedDenominator)
    documentNormalizedDenominator[d]=documentNormalizedDenominator[d]**0.5

#print (documentNormalizedDenominator)


#obtain score now by multiplying the queryWeights and documentWeights
#finally obtain score
#score according to documents


for q in queryWt:#for every word in query_wt
    if q in megadict:
        #now parse all documents
        innerDict = megadict[q]
        for i in innerDict:
            score[i] += queryWt[q]*(innerDict[i]['6']/documentNormalizedDenominator[i])

print (score)

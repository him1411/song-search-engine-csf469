import os
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

queryStr = ""

class main_class(object):

    
    corpusSize=1000
    vocabulary = {}
    vocabulary_idf = {}
    freqDist = {}
    document_tokens_list= []
    temp_doc_tokens = []
    snowball_stemmer = SnowballStemmer('english')
    docFiles = [f for f in os.listdir('./corpus') if f.endswith(".txt")]
    docFiles.sort()

    def __build_vocabulary(document_tokens):
            vocabulary_index=len(vocabulary)-1
            for word in document_tokens:
                # if word not in vocabulary_idf:
                #     vocabulary_idf[word] = 1 #vocabulary_idf is the frequency of the words in rthe document
                # else:
                #     vocabulary_idf[word] = vocabulary_idf[word] + 1

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
            for word in dohota_cument_tokens:
                vocabulary_idf

    def returnTermFrequency(term, document_tokens, document_tokens_index):
        return math.log2(1+(freqDist[document_tokens_index][term]/float(len(document_tokens))))

    def returnIdf(term):
        return math.log2(len(document_tokens_list)/vocabulary_idf[term])




    def terminal_function():
        """
        Function for inputting query and performing query based operations and finally calculating cosine scores
        """
        with open('./savers/document_tokens_list.json') as json_data:
            document_tokens_list = json.load(json_data)

        with open('savers/vocabulary.json') as json_data:
            vocabulary = json.load(json_data)

        with open('savers/primeDictionary.json') as json_data:
            primeDictionary = json.load(json_data)

        score={}

        #Applying stemming porting on queryf documents that a term 't' occurs in and N is the total number of documents in the collection. Some
        
        words = queryStr
        temp_doc_tokens = nltk.word_tokenize(words)
        temp_doc_tokens = [w.lower() for w in temp_doc_tokens]
        #temp_doc_tokens = [main_class.snowball_stemmer.stem(token) for token in temp_doc_tokens]
        #temp_doc_tokens = [token for token in temp_doc_tokens if token not in nltk.corpus.stopwords.words('english')]
        #document_tokens_list.append(temp_doc_tokens)
        print(temp_doc_tokens)
        queryList = temp_doc_tokens
        print(queryList)
        print('retro')

        for i in range(0,19):
            s = 0.0
            print(i)
            for word in queryList:
                s = s + primeDictionary[word][str(i)][str(3)]
            print(s)

        print('retro')

        numOfWords = 0
        #print (queryList)
        queryDict={} #contains frequency till here i.e the tf
        #calculating frequency
        for q in queryList:
            numOfWords = numOfWords + 1
            if q not in queryDict:
                queryDict[q]=0
            queryDict[q]+=1
    
        print (queryDict)

        queryDf={}
        #Getting total Document frequency of the word
        for qkey,qvalue in queryDict.items():
            if qkey in primeDictionary:#now here we have one document , we have to sum over multiple documents
                innerDict = primeDictionary[qkey]
                total_frequency_of_documents=0
                for i in innerDict:
                    if(innerDict[i]['1']>0):
                        total_frequency_of_documents+=1
                queryDf[qkey]=total_frequency_of_documents
            else:
                queryDf[qkey]=0
        print('query Df')
        print(queryDf)

        

        queryIdf={}
        #check all formulae here
        for q in queryDf:
            #if (queryDf[q]!=0):
                queryIdf[q] = math.log((main_class.corpusSize/queryDf[q]))
            #else:
             #   queryIdf[q] = 1+math.log((main_class.corpusSize/1+queryDf[q]),10)

        for q in queryDict:
            queryDict[q] = math.log(1+(queryDict[q]/float(numOfWords)))

        print(queryDict)
        print('***')

        print(queryIdf)
        #tfWeighting - multiplying tf-raw i.e. tf and Idf

        queryWt={}
        for q in queryIdf:
            queryWt[q]=queryIdf[q]* queryDict[q]

        print (queryWt)

        queryNormalizedDenomator=0
        for q in queryWt:
            queryNormalizedDenomator+=queryWt[q]*queryWt[q]

        #print (queryNormalizedDenomator)
        queryNormalizedDenomator=(queryNormalizedDenomator)**0.5

        queryNormalized={}
        for q in queryWt:
            queryNormalized[q] = queryWt[q]/queryNormalizedDenomator

        #print (queryNormalized)


       
        documentNormalizedDenominator={}
        score = {}
        #initializing all documentNormalizedDenominator to zero
        for q in primeDictionary:
            innerDict=primeDictionary[q]
            #print(q)
            for i in innerDict:
                documentNormalizedDenominator[i]=0
                score[i]=0

        for q in primeDictionary:
            innerDict=primeDictionary[q]
            #print(q)
            for i in innerDict:
                documentNormalizedDenominator[i]+=(math.pow(innerDict[i]['3'],2))
            

        for d in documentNormalizedDenominator:
            
            documentNormalizedDenominator[d]=documentNormalizedDenominator[d]**0.5
        


        for q in queryWt:#for every word in query_wt
            if q in primeDictionary:
                #now parse all documents
                innerDict = primeDictionary[q]
                for i in innerDict:
                    score[i] += queryWt[q]*(innerDict[i]['3']/documentNormalizedDenominator[i])

        with open('savers/store.json', 'w') as fp:
            json.dump(score, fp)



    def process_function(query):
        print('>>>>>')
        print(query)
        global queryStr
        queryStr = query
        main_class.terminal_function()
        
        #find max wala function#######################
        with open('savers/store.json') as json_data:
            score = json.load(json_data)
        sorted_score = sorted(score, key=score.get, reverse=True)
        docFiles = [f for f in os.listdir('./corpus') if f.endswith(".txt")]
        docFiles.sort()
        for i in sorted_score[:10]:
            print(i)
        
        #end of find max################################

        linkNumber_list = sorted_score[:10]
        docList = []
        docList.clear()
        f = open("songname.txt")
        data = f.read()
        data = data.split("\n")
        print(linkNumber_list)
        for linkNum in linkNumber_list:
            docList.append(data[int(linkNum)]);
        print(docList)
        return docList


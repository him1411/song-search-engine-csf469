from scipy.sparse import csr_matrix
from scipy.sparse import linalg
from scipy.sparse.linalg import eigsh
from scipy import sparse
import pandas as pd
import numpy as np
import math
import time

user_id=[]
user_id_list=[]
movie_id_list=[]
ratings_list=[]

def loadMovieLens(path='./u.data'):
# Get movie titles
    movies={}
    #will use the movie title in the next loop
    for line in open('./u.item'):
        (id,title)=line.split('|')[0:2]
        movies[id]=title
# Load data
    prefs={}
    for line in open('./data/ua.base'):
        (user,movieid,rating,ts)=line.split('\t')

        user_id.append(user)

        #getting unique user ids
        if user not in user_id_list:
            user_id_list.append(user)

        #getting unique movie ids
        if movieid not in movie_id_list:
            movie_id_list.append(movieid)

        #getting the list of all the ratings
        ratings_list.append(rating)

        prefs.setdefault(user,{})
        #setting key and its value as a dictionary
        #print prefs
        prefs[user][movies[movieid]]=float(rating)
    return prefs


def loadMovieLensTest(path='./u.data'):
# Get movie titles
    movies={}
    #will use the movie title in the next loop
    for line in open('./u.item'):
        (id,title)=line.split('|')[0:2]
        movies[id]=title
# Load data
    prefs={}
    for line in open('./data/ua.test'):
        (user,movieid,rating,ts)=line.split('\t')

        user_id.append(user)

        #getting unique user ids
        if user not in user_id_list:
            user_id_list.append(user)

        #getting unique movie ids
        if movieid not in movie_id_list:
            movie_id_list.append(movieid)

        #getting the list of all the ratings
        ratings_list.append(rating)

        prefs.setdefault(user,{})
        #setting key and its value as a dictionary
        #print prefs
        prefs[user][movies[movieid]]=float(rating)
    return prefs


#loadMovieLens()
#print (len(user_id_list))
#print (len(movie_id_list))

#m=len(user_id_list)
#n=len(movie_id_list)
#print (len(ratings_list))

#row = user_id.astype('category', categories=user_id_list).cat.codes
#print (row)

#using pandas for the same
"""dataframe = pd.read_csv('./u.data', sep='\t')
dataframe.columns=['userId','movieId','rating','timestamp']
#print (dataframe)
userIdl = list(dataframe.userId.unique())
movieIdl = list(dataframe.movieId.unique())
row = dataframe.userId.astype('category', categories=userIdl).cat.codes
#print (type(row))
col = dataframe.movieId.astype('category', categories=movieIdl).cat.codes
#creating the sparse matrix
#print (col)
data=dataframe['rating'].tolist()
m=len(userIdl)
n=len(movieIdl)
A =  csr_matrix((data,(row,col)),shape = (m,n) , dtype = np.float64)
A_t = csr_matrix(A.transpose())
#print ((A))
A_At=A* A_t
At_A=A_t*A
"""
prefTest=loadMovieLensTest()
prefTrain=loadMovieLens()

for i in prefTest['87']:
    if i not in prefTrain['87']:
        print i

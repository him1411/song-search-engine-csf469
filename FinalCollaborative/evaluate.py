import pickle
import math
import scipy.stats

with open('rankings.p', 'rb') as f:
    rankings = pickle.load(f)

def loadTestData(path='./u1.test'):
# Get movie titles
    movies={}
    #will use the movie title in the next loop
    for line in open('../u.item'):
        (id,title)=line.split('|')[0:2]
        movies[id]=title
# Load data
    prefs={}
    for line in open('../data/ua.test'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        #setting key and its value as a dictionary
        #print prefs
        prefs[user][movies[movieid]]=float(rating)
    return prefs

def calculateRMSE(trainData,testData):
    rmse=0
    count = 0
    sum=0
    for user in testData:
        for movie in testData[user]:
            if movie in trainData[user]:
                sum+=(trainData[user][movie] - testData[user][movie])**2
                count+=1
    rmse = math.sqrt(sum/count)
    return rmse

def findPrecisiononTopK(raknings,testData):
    num=0
    k=0
    den=0
    total_ranking_list=[]
    for user in testData:
        for movie in testData[user]:
            if testData[user][movie]>=3.5:
                k+=1
                if movie in rankings[user]:
                    if rankings[user][movie]>=3.5:
                        num+=1
    for user in rankings:
        for movie in rankings[user]:
            total_ranking_list.append(rankings[user][movie])
    total_ranking_list.sort()
    total_ranking_list.reverse()
    for val in total_ranking_list[0:k]:
        if val>=3.5:
            den+=1
    #print num
    #print den
    return float(num)/float(den) * 100
    #return num/den




def check(trainData,testData):
    count=0
    for user in testData:
        for movie in testData[user]:
            if movie not in trainData[user]:
                count+=1
    return count

def spearmans_rank_correlation(trainData,testData):
    sum_of_correlations=0
    count =0
    for user in testData:
        count+=1
        trainList=[]
        testList=[]
        trainList_ranked = []
        testList_ranked = []
        for movie in testData[user]:
            if movie in trainData[user]:
                trainList.append(trainData[user][movie])
                testList.append(testData[user][movie])
                #testList.sort()
                #trainList.sort()
                #trainList.reverse()
                #testList.reverse()
                trainList_ord = sorted(trainList)
                testList_ord = sorted(testList)

        for i in range(len(trainList)):
	                trainList_ranked.append([trainList[i],trainList_ord.index(trainList[i])+1])

        for i in range(len(testList)):
	                testList_ranked.append([testList[i],testList_ord.index(testList[i])+1])


        d = []
        for i in range(len(trainList_ranked)):
	    d.append(trainList_ranked[i][1] - testList_ranked[i][1])
        #print d

        # calculate d^2
        d_sq = [i**2 for i in d]
        #print d_sq

        # sum d^2
        sum_d_sq = sum(d_sq)
        #print sum_d_sq

        # calculating n^3 - n
        den = len(trainList)**3 - len(trainList)
        #print n_cu_min_n

        # calculate rho
        rho = 1 - ((6.0*sum_d_sq)/den)
        #print rho
        sum_of_correlations += rho

    return (sum_of_correlations/count)

def spearmans_rank(trainData,testData):
    set_1=[]
    set_2 =[]

    for user in trainData:
        for movie in trainData[user]:
            set_1.append(trainData[user][movie])

    for user in testData:
        for movie in testData[user]:
            set_2.append(testData[user][movie])

    set_1_ord = sorted(set_1)
    set_2_ord = sorted(set_2)

    set_1_ranked = []
    set_2_ranked = []

    for i in range(len(set_1)):
	    set_1_ranked.append([set_1[i], set_1_ord.index(set_1[i])+1])

    for i in range(len(set_2)):
	    set_2_ranked.append([set_2[i], set_2_ord.index(set_2[i])+1])

    d = []
    for i in range(len(set_1_ranked)):
	    d.append(set_1_ranked[i][1] - set_2_ranked[i][1])


# calculate d^2
    d_sq = [i**2 for i in d]


# sum d^2
    sum_d_sq = sum(d_sq)

# calculate n^3 - n
    n_cu_min_n = len(set_1)**3 - len(set_1)

    rho = 1 - ((6.0*sum_d_sq)/n_cu_min_n)
    return rho

testData=loadTestData()
#print (len(rankings))

print (calculateRMSE(rankings,testData))

#print (check(rankings,testData))

#print (spearmans_rank_correlation(rankings,testData))
#print rankings['344']

print (findPrecisiononTopK(rankings,testData))

print (spearmans_rank(rankings,testData))

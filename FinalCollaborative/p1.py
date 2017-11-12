"""import math
import pickle
def sim_pearson(prefs,p1,p2):
    # Finding the list of all the items which are simiar for p1 and p2
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    # Find the number of elements
    n=len(si)
    # if they are no ratings in common, return 0
    if n==0:
        return 0
     # Add up all the ratings
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    # Sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
    # Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    # Calculate Pearson score
    num=pSum-(sum1*sum2/n)
    den=math.sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r

def getRecommendedations(prefs,itemMatch,user):
    #storing all the userRatings of a particuar user in userRatings
    userRatings=prefs[user]
    scores={}
    totalSim={}
# Loop over items rated by this user
    for (item,rating) in userRatings.items( ):
# Loop over items similar to this one
        for (similarity,item2) in itemMatch[item]:
# Ignore if this user has already rated this item
            if item2 in userRatings: continue
# Weighted sum of rating times similarity
            #if item2 found set to item2 else 0
            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating
# Sum of all the similarities
            totalSim.setdefault(item2,0)
            totalSim[item2]+=similarity
    # Divide each total score by total weighting to get an average
    rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
# Return the rankings from highest to lowest
    rankings.sort( )
    rankings.reverse( )
    return rankings

def calculateSimilarity(prefs,n=40):
# Create a dictionary of items showing which other items they
# are most similar to.
    result={}
# Invert the preference matrix to be item-centric
    #itemPrefs=transformPrefs(prefs)
    c=0
    for item in prefs:
# Status updates for large datasets
        c+=1
        if c%100==0: print "%d / %d" % (c,len(prefs))
# Find the most similar items to this one
        scores=topMatches(prefs,item,n=n,similarity=sim_pearson())
        result[item]=scores
    return result

def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
    for other in prefs if other!=person]
# Sort the list so the highest scores appear at the top
    scores.sort( )
    scores.reverse( )
    return scores[0:n]

def loadMovieLens(path='./u.data'):
# Get movie titles
    movies={}
    #will use the movie title in the next loop
    for line in open('../u.item'):
        (id,title)=line.split('|')[0:2]
        movies[id]=title
# Load data
    prefs={}
    for line in open('../data/ua.base'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        #setting key and its value as a dictionary
        #print prefs
        prefs[user][movies[movieid]]=float(rating)
    return prefs

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

def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    rankings={}
    for other in prefs:
    # compare all other users except himself
        if other==person: continue
    #finding similarity of the user with every other user
        sim=similarity(prefs,person,other)
    #not using less than or equal to zero similarity
        if sim<=0: continue
        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item]==0:
            # Similarity * Score
                #item here is the key
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
# Sum of similarities
                simSums.setdefault(item,0)
                simSums[item]+=sim
# Create the normalized list
    #rankings=[((total/simSums[item]),item) for item,total in totals.items( )]
    rankings[person]={}
    for item in totals:
    #rankings[person] = totals[item]/simSums[item]
        rankings[person][item]=totals[item]/simSums[item]
    return rankings

trainData = loadMovieLens()
testData = loadTestData()
ratings={}
i=0
for user in trainData:
    i+=1
    print i
    ratings[user]=getRecommendations(trainData,user)
#rankings = getRecommendations(trainData,'87')
#print rankings

f=open('./ratings.p','w')
pickle.dump(ratings, f)
f.close()

"""

from math import sqrt
import math
import time
import pickle
recommendedList={}
rankings={}
def sim_pearson(prefs,p1,p2):
    #print(type(p1))
    #print (type(p2))
    # Finding the list of all the items which are simiar for p1 and p2
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    # Find the number of elements
    n=len(si)
    # if they are no ratings in common, return 0
    if n==0:
        return 0
     # Add up all the ratings
    """sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    # Sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
    # Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    # Calculate Pearson score
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den"""
    #my pearson score rating
    mean_p1=sum([prefs[p1][it] for it in prefs[p1]])/len(prefs[p1])
    mean_p2=sum([prefs[p2][it] for it in prefs[p2]])/len(prefs[p2])
    den_p1 = math.sqrt(sum([(math.pow((prefs[p1][it] - mean_p1 ),2) )for it in si]))
    den_p2 = math.sqrt(sum([(math.pow((prefs[p2][it] - mean_p2 ),2)) for it in si]))
    num = sum([((prefs[p1][it] - mean_p1)*(prefs[p2][it] - mean_p2)) for it in si])
    den =den_p1*den_p2
    if(den == 0): return 0
    r = num/den
    return r

def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
    for other in prefs if other!=person]
# Sort the list so the highest scores appear at the top
    scores.sort( )
    scores.reverse( )
    return scores[0:n]

# Gets recommendations for a person by using a weighted average
# of every other user's rankings
#get Recommendations based on User-User Collaborative Filtering
def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
    # compare all other users except himself
        if other==person: continue
    #finding similarity of the user with every other user
        sim=similarity(prefs,person,other)
    #not using less than or equal to zero similarity
        if sim<=0: continue
        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item]==0:
            # Similarity * Score
                #item here is the key
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
# Sum of similarities
                simSums.setdefault(item,0)
                simSums[item]+=sim
# Create the normalized list
    #rankings=[((total/simSums[item]),item) for item,total in totals.items( )]
    rankings[person]={}
    for item in totals:
    #rankings[person] = totals[item]/simSums[item]
        rankings[person][item]=totals[item]/simSums[item]
    #print (len(rankings))
# Return the sorted list
    #important for top k and spearman
    #rankings.sort( )
    #rankings.reverse( )


###optional to append , but needed for finding the rmse error###
    #print (len(prefs[person]))


    #for pred in rankings:
     #   prefs[person][pred[1]]=pred[0]
    return rankings
    #print (len(prefs[person]))



def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
# Flip item   and person
            result[item][person]=prefs[person][item]
    return result


def calculateSimilarItems(prefs,n=10):
# Create a dictionary of items showing which other items they
# are most similar to.
    result={}
# Invert the preference matrix to be item-centric
    itemPrefs=transformPrefs(prefs)
    c=0
    for item in itemPrefs:
# Status updates for large datasets
        c+=1
        if c%100==0: print "%d / %d" % (c,len(itemPrefs))
# Find the most similar items to this one
        scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
        result[item]=scores
    return result

def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
    # compare all other users except himself
        if other==person: continue
    #finding similarity of the user with every other user
        sim=similarity(prefs,person,other)
    #not using less than or equal to zero similarity
        if sim<=0: continue
        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item]==0:
            # Similarity * Score
                #item here is the key
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
# Sum of similarities
                simSums.setdefault(item,0)
                simSums[item]+=sim
# Create the normalized list
    #rankings=[((total/simSums[item]),item) for item,total in totals.items( )]
    rankings[person]={}
    for item in totals:
    #rankings[person] = totals[item]/simSums[item]
        rankings[person][item]=totals[item]/simSums[item]
    #print (len(rankings))
# Return the sorted list
    #important for top k and spearman
    #rankings.sort( )
    #rankings.reverse( )

def loadMovieLens(path='./u.data'):
# Get movie titles
    movies={}
    #will use the movie title in the next loop
    for line in open('../u.item'):
        (id,title)=line.split('|')[0:2]
        movies[id]=title
# Load data
    prefs={}
    for line in open('../data/ua.base'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        #setting key and its value as a dictionary
        #print prefs
        prefs[user][movies[movieid]]=float(rating)
    return prefs

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

def getMeanRatings(prefs):
    meanRatings = {}
    for user in prefs:
        count = 0
        sum = 0
        for item in prefs[user]:
            sum += prefs[user][item]
            count += 1
        meanRatings[user]=sum/count
    return meanRatings

#function to subtract mean ratings
def subMeanRatings(prefs,meanRatings):
    for user in prefs:
        for item in prefs[user]:
            prefs[user][item] -= meanRatings[user]

    return prefs

#function to again add mean ratings
def addMeanRatings(prefs,meanRatings):
    for user in prefs:
        for item in prefs[user]:
            prefs[user][item] += meanRatings[user]
    return prefs

trainData=loadMovieLens()
testData= loadTestData()
meanRatings = getMeanRatings(loadMovieLens())
trainData=subMeanRatings(loadMovieLens(),meanRatings)

#getRecommendations(trainData,'100')
#addMeanRatings(rankings,meanRatings)
#print rankings

start = time.clock()
for i in range(1,944):
    print (i)
    getRecommendations(trainData,str(i))
end = time.clock()

print (start - end)

addMeanRatings(rankings,meanRatings)
#print rankings

f=open('./rankings.p','w')
pickle.dump(rankings, f)
f.close()

#getRecommendations(trainData,str)
#getRecommendations(trainData,'87')
#print rankings


#print getRecommendations(trainData,'87')

#print (len(prefs))
#initially 210
#print (len(prefs['87']))
#print prefs['87']
#now has 1446 more recommendations

#itemsim=calculateSimilarItems(prefs,n=50)
#print (getRecommendedItems(prefs,itemsim,'87'))[0:10]
#print (prefs)
#print (len(prefs['87']))
#gives the numbe
#mean_p1=sum([(prefs['87'][it])for it in prefs['87']])/len(prefs['87'])
#print (mean_p1)

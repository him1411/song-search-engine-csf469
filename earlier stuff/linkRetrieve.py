import os

linkNumber_list = [4,3,6,75,34,12,10,2,9,1]
docList = []
docList2 = []
x=0
for linkNum in linkNumber_list:
    x=0
    with open('linksCorpus.txt') as f:
        for line in f:
            if(x==linkNum):
                docList.append(line)
                break
            x+=1

print(docList)

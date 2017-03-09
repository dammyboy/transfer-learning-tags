from __future__ import division
import csv 

KnowledgeAreas = ['biology', 'cooking', 'crypto', 'diy', 'robotics','travel']

TextAndTags = []

for k in KnowledgeAreas:
    count = 0
    with open('data/'+k+'.csv') as datafile:
        dataReader = csv.reader(datafile)
        for ktags in dataReader:
            if not count:
                count +=1
            else:
                curRow = {'Area': k}
                curRow['Title'] = ktags[1]
                curRow['Content'] = ktags[2]
                tempTags = []
                
                curTags = ktags[3].split()
                for tag in curTags:
                    tag_ = tag.replace('-', ' ')
                    tempTags.append(tag_)
                
                curRow['Tags'] = tempTags
                TextAndTags.append(curRow)

x=1               
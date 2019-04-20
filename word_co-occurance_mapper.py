#!/usr/bin/env python

import sys

#words that we want to find the co-occurance for
tophits=["nba", "basketball", "kobe", "jordan", "durant","star","michael", "bryant", "kevin", "shaq","o","neil","lebron","james","Lakers", "championship"]

textfile=[]
word1 = None

word2 = None

for line in sys.stdin:
    #remove leading and trailing white spaces
    line= line.strip()
    #populating an array of words from each line
    for word in line.split():
        textfile.append(word)

a=len(textfile)

#this will search if the two words present in the top hits co-occur with words distance from each other
for i in range(0,a-20):
    if(textfile[i] in tophits):
        word1 = textfile[i]
        for j in range (1,20):
            if(textfile[i+j] in tophits):
                word2 = textfile[i+j]
                if(word1!=word2):
                    print('%s|%s\t %s'%(word1,word2,1))

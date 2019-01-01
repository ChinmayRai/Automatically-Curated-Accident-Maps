import json
from jpype import *
import sys

cpopt="-Djava.class.path=%s" % ("/Users/samarthaggarwal/Documents/SURA/processing/openie_trials")
startJVM(getDefaultJVMPath(),"-ea",cpopt)
td = JClass('time.time_detect')
ext=td.extract

def deduplicate(l):
	l1=[]
	for i in l:
		if i not in l1 and i!="":
			l1.append(i)

	return l1

infile="temp_files/prep_clauses_merged.json"
jsonTimeOutfile="temp_files/time.json"
jsonReducedClauseOutFile="temp_files/prep_clauses_merged_reduced.json"

file_object = open(infile,"r")
article = file_object.read()
article = json.loads(article)
file_object.close()


# j=1	#date
date=int(sys.argv[1])
mon=int(sys.argv[2])
year=int(sys.argv[3])

# for j in range(0,len(month)):
	# day=month[j]
	# for article in day:
updatedArticle=[]
for i in range(0,len(article)):
	sents=article[i]
	newSentence=[]
	newSentence.append(sents[0])
	loc=[]
	nonTime=[]
	for c in sents[1]:
		temp = ext(c,date,mon,year)
		if (len(temp)>0):
			loc.append(temp)
		else:
			nonTime.append(c)
	newSentence.append(nonTime)
	updatedArticle.append(newSentence)
	sent=sents[0]
	sents=[]
	sents.append(sent)

	if loc!=[] :
		sents.append(deduplicate(loc))
	
	article[i]=sents


# for day in month:
	# for article in day:
time=[]
for i in range(0,len(article)):
	if(len(article[i])==2):
		for j in range(0,len(article[i][1])):
			time=time+article[i][1][j].split("\t")
		article[i]=[article[i][0]]
article.append(deduplicate(time))



# file_object = open(jsonTimeOutfile,"w+")
# file_object.close()

with open(jsonTimeOutfile, 'w+') as outfile:
    json.dump(article, outfile)	

# file_object = open(jsonReducedClauseOutFile,"w+")
# file_object.close()

with open(jsonReducedClauseOutFile, 'w+') as outfile:
    json.dump(updatedArticle, outfile)	

shutdownJVM()
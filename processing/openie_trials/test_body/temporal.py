import json
from jpype import *
cpopt="-Djava.class.path=%s" % ("/home/chinmay/Documents/SURA/processing/openie_trials")
startJVM(getDefaultJVMPath(),"-ea",cpopt)
td = JClass('time.time_detect')
ext=td.extract



mon=7
year=2017


def deduplicate(l):
	l1=[]
	for i in l:
		if i not in l1 and i!="":
			l1.append(i)

	return l1

infile="july2017/july_prep_clauses_merged.json"

file_object = open(infile,"r")
month = file_object.read()
month = json.loads(month)
file_object.close()


for j in range(0,len(month)):
	day=month[j]
	for article in day:
		for i in range(0,len(article)):
			sents=article[i]

			loc=[]
			for c in sents[1]:
				if (len(ext(c,j+1,mon,year))>0):
					loc.append(ext(c,j+1,mon,year))

			sent=sents[0]
			sents=[]
			sents.append(sent)

			if loc!=[] :
				sents.append(deduplicate(loc))
			
			article[i]=sents


for day in month:
	for article in day:
		time=[]
		for i in range(0,len(article)):
			if(len(article[i])==2):
				for j in range(0,len(article[i][1])):
					time=time+article[i][1][j].split("\t")
				article[i]=[article[i][0]]
		article.append(deduplicate(time))




jsonOutfile="july2017/july_time.json"

file_object = open(jsonOutfile,"w+")
file_object.close()

with open(jsonOutfile, 'w+') as outfile:
    json.dump(month, outfile)	


shutdownJVM()
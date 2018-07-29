import json
from jpype import *
cpopt="-Djava.class.path=%s" % ("/home/chinmay/Documents/SURA/processing/openie_trials")
startJVM(getDefaultJVMPath(),"-ea",cpopt)
td = JClass('time.time_detect')

def deduplicate(l):
	l1=[]
	for i in l:
		if i not in l1:
			l1.append(i)

	return l1

infile="july2017/july_prep_clauses_merged.json"

file_object = open(infile,"r")
month = file_object.read()
month = json.loads(month)
file_object.close()


for day in month:
	for article in day:
		for i in range(0,len(article)):
			sents=article[i]
			loc=[]
			for c in sents[1]:
				if (td.extract(c)!=""):
					loc.append(td.extract(c))

			sent=sents[0]
			sents=[]
			sents.append(sent)
			if loc!=[] :
				sents.append(deduplicate(loc))
			
			article[i]=sents


jsonOutfile="july2017/july_loc.json"

file_object = open(jsonOutfile,"w+")
file_object.close()

with open(jsonOutfile, 'w+') as outfile:
    json.dump(month, outfile)	


shutdownJVM()
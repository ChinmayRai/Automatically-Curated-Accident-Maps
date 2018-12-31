# DESCRIPTION : from the list of clauses broken up on prepositions, this function deduplicates them and converts them to utf-8 encoding

import json

def deduplicate(l):
	l1=[]
	for i in l:
		if i not in l1:
			l1.append(i)

	return l1

inFile="sent_selected.json"
jsonOutfile="prep_clauses_merged.json"

file_object = open(inFile,"r")
article = file_object.read()
article = json.loads(article)
file_object.close()

# for day in month:
	# for article in day:
for i in range(0,len(article)):
	sents=article[i]
	l=[]

	for j in range(1,len(sents)):
		for k in sents[j]:
			k=k.encode('utf-8')
		l=l+sents[j]

	l=deduplicate(l)

	sent=sents[0].encode('utf-8')
	sents=[]
	sents.append(sent)
	sents.append(l)
	article[i]=sents


file_object = open(jsonOutfile,"w+")
file_object.close()


with open(jsonOutfile, 'w+') as outfile:
    json.dump(article, outfile)	


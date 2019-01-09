# DESCRIPTION : selects the word that is a noun from the list of july_prep_clauses_merged

import json
from nltk import word_tokenize,pos_tag

#gives list of POS tagged words of sentence x in form of (word,POS)
def pos(x):
	text=word_tokenize(x)
	k=pos_tag(text)
	for i in range(len(k)):
		k[i] = tuple([k[i][0].lower(), k[i][1]]);
	return k

#gives the POS tag of word s from list l
def tag(l,s):
	sr=""
	for e in l:
		if (e[0]==s):
			sr=e[1]
	if (sr==""):
		return "!"
	else:
		return sr

inFile="temp_files/prep_clauses_merged_reduced.json"
jsonOutfile="temp_files/prop_noun_clauses.json"

file_object = open(inFile,"r")
article = file_object.read()
article = json.loads(article)
file_object.close()

selectedTags=['NNP', 'NNPS']
verbTags=['VB','VBD','VBG','VBN','VBP','VBZ']
# for day in month:
# 	for article in day:
for sent in article:
	l=pos(sent[0])
	l1=sent[1]
	l2=[]
	for e in l1:
		if (len(word_tokenize(e))>5):
			continue
		else:
			ll=word_tokenize(e)
			n=0
			for r in ll:
				if (tag(l,r)=='NNP' or  tag(l,r)=='NNPS'):
					n=1
			for r in ll:
				if(tag(l,r) in verbTags):
					n=0

			if (n==1):
				l2.append(e)

	sent[1]=l2


# file_object = open(jsonOutfile,"w+")
# file_object.close()


with open(jsonOutfile, 'w+') as outfile:
    json.dump(article, outfile)
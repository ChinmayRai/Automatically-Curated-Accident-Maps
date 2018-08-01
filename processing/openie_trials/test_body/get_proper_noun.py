import json
from nltk import word_tokenize,pos_tag

#gives list of POS tagged words of sentence x in form of (word,POS)
def pos(x):
	text=word_tokenize(x)
	k=pos_tag(text)
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

inFile="july2017/july_prep_clauses_merged.json"

file_object = open(inFile,"r")
month = file_object.read()
month = json.loads(month)
file_object.close()

for day in month:
	for article in day:
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

					if (n==1):
						l2.append(e)

			sent[1]=l2



jsonOutfile="july2017/july_prop_noun_clauses.json"

file_object = open(jsonOutfile,"w+")
file_object.close()


with open(jsonOutfile, 'w+') as outfile:
    json.dump(month, outfile)	
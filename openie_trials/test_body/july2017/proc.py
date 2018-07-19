import json
from nltk.stem.wordnet import WordNetLemmatizer

def trim(s):
	i=0
	if (len(s)==0 or s==" "):
		return s;
	while(i<len(s) and s[i]==" "):
		i+=1
	l=len(s)-1
	while(s[l]==" "):
		l-=1
	return s[i:l+1]


def extract(l):
	lem = WordNetLemmatizer()

	stopWords = ["get","have","'s","up","down","towards","off","to","have","also","over","after","outside","near","the","a"]
	rootVerbs = []
	if (l[0]=='['):
		return ["fact"]
	verbWords = l.lower().split(" ")
	lemWords = []
	for i in range(len(verbWords)):
		lemWords.append(lem.lemmatize(verbWords[i],'v'))

	i=0;
	while(i<len(lemWords)):
		if(lemWords[i]=="be"):
			break;
		i+=1

	i+=1
	if(i==len(lemWords)):
		lemWords.pop()
	elif(i>len(lemWords)):
		i=0

		# not printing the adverbs, prepositions and other stop words
	while(i<len(lemWords)):
		word=lemWords[i]
		l=len(word)
		if(not( (word[l-2]=='l' and word[l-1]=='y') or (word in stopWords) )):
			# print word,
			rootVerbs.append(word)
		i+=1
	for vb in rootVerbs:
		vb=str(vb)
	return rootVerbs



def cook(tup):
	if(tup[0]=="("):
		tup=tup[1:-2]
	elif(tup[:7]=="Context"):
		i=0
		while(tup[i]!=":"):
			i+=1
		tup=tup[i+2:-2]
	arr=tup.split(";")
	for i in range(len(arr)):
		arr[i]=str(trim(arr[i]))
	print (extract(arr[1]),arr[2:])
	for i in range(2,len(arr)):
		if(arr[i][0:2]=="T:"):
			print arr[i]
		if(arr[i][0:2]=="L:"):
			print arr[i]



file_object = open(r"july_sent_selected.json","r")
month = file_object.read()
month = json.loads(month)
file_object.close()

for day in month:
	for article in day:
		for sents in article:
			for trip in sents:
				if (trip[0]=="0"):
					cook(trip[5:])
			print
			print
		print"----------------------------------------------------------------------------"
	print "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

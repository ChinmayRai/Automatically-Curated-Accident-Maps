from nltk.stem.wordnet import WordNetLemmatizer
import json

def freq_dist(samples):
	freq = dict()
	for word in samples:
		if word in freq.keys():
			freq[word]+=1
		else:
			freq[word]=1

	return freq


# file_object = open(r"out.txt","r")
file_object = open(r"july_openie_output.txt","r")
# month = file_object.read()
# month = json.loads(month)

lines = file_object.readlines()
file_object.close()

lem = WordNetLemmatizer()

stopWords = ["get","have","'s","up","down","towards","off","to","have","also","over","after","outside","near","the","a"]
rootVerbs = []

for line in (lines):
	if(line[0]=='0' and line[1]=='.'):

	# extracting second clause from openIE's output
		verb = ""
		i=0
		while(line[i]!=";"):
			i+=1
		i+=2;
		while(line[i]!=";"):
			verb += line[i]
			i+=1

	# ignoring factual clauses
		if(verb[0]=='['):
			continue

	# breaking clause into list of words and lemmatizing
		verbWords = verb.lower().split(" ")
		# for word in verbWords:
		# 	print word,
		# print " -> ",

		lemWords = []
		for i in range(len(verbWords)):
			lemWords.append(lem.lemmatize(verbWords[i],'v'))

		# for word in lemWords:
		# 	print word,
		# print " -> ",

	# printing part which lies after "be" part of verb
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
		# print

		# print "==="

	# elif(line[0]=='-'):
	# 	print "-------------------------"
	# elif(line[0]=='+'):
	# 	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"


rootVerbSet = set(rootVerbs)
# print "Size of set = ",len(rootVerbSet)
# for i in rootVerbSet:
# 	print i

# for json output
with open('unique_root_verbs.json', 'w+') as outfile:
    json.dump(list(rootVerbSet), outfile)


rootVerbFreq = freq_dist(rootVerbs)
# print rootVerbFreq

# for i in rootVerbFreq:
# 	print i, '\t', rootVerbFreq[i]

rootVerbSorted = []

for w in sorted(rootVerbFreq, key=rootVerbFreq.get, reverse=True):
	print rootVerbFreq[w], w
	rootVerbSorted.append(w)


# to print json of root verbs with their frequency
with open('freq_dist.json', 'w+') as outfile:
    json.dump(rootVerbFreq, outfile)


# to print json of root verbs in decreasing order of frequency
with open('root_verbs_sorted.json', 'w+') as outfile:
    json.dump(rootVerbSorted, outfile)

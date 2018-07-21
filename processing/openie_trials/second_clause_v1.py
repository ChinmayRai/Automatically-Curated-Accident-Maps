from nltk.stem.wordnet import WordNetLemmatizer

# file_object = open(r"out.txt","r")
file_object = open(r"May_2017_IE.txt","r")
# month = file_object.read()
# month = json.loads(month)

lines = file_object.readlines()
file_object.close()

lem = WordNetLemmatizer()

stopWords = ["get","have","'s","up","down","towards","off","to","have","also","over","after","outside","near","the","a"]

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
		for word in verbWords:
			print word,
		print " -> ",

		lemWords = []
		for i in range(len(verbWords)):
			lemWords.append(lem.lemmatize(verbWords[i],'v'))

		for word in lemWords:
			print word,
		print " -> ",

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
				print word,
			i+=1
		print

		# print "==="

	elif(line[0]=='-'):
		print "-------------------------"
	elif(line[0]=='+'):
		print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
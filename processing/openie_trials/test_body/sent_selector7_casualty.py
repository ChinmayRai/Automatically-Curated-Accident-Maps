import json
import sys
from nltk.stem.wordnet import WordNetLemmatizer
# from root_verb_extractor import extract

# returns the common elements in the 2 lists
def intersection(l1,l2):
	intersection=[]
	for i in l1:
		if(i in l2):
			# return True
			intersection.append(i)

	# return False
	return intersection

# removes extra spaces from edges of string
def trim(s):
	i=0
	l=len(s)-1
	try:
		while(i<=l and s[i]==" "):
			i+=1
		while(l>=i and s[l]==" "):
			l-=1
		if(i>l):
			return ""
		else:
			return s[i:l+1]

	except Exception as e:
		print e
		print "string=",s,"=over"


# converts openie output sentence to tuple, returns False if sentence is not a tuple
def get_tuple(s):
	if(not( (s[0]=="0" or s[0]=="1" ) and s[1]==".")):
		return False
	tup=s[5:-1]	# -1 to remove \n from the end
	if(tup[0]=="("):
		tup=tup[1:-1]
	elif(tup[:7]=="Context"):
		i=0
		while(tup[i]!=":"):
			i+=1
		tup=tup[i+2:-1]

	arr=tup.split(";")

	for i in range(len(arr)):
		arr[i]=trim(arr[i])

	return tuple(arr)


# returns root verbs occuring in all tuples of a sentence
def root_verbs(sentence):
	lem = WordNetLemmatizer()

	stopWords = ["get","have","'s","up","down","towards","off","to","have","also","over","after","outside","near","the","a"]
	rootVerbs = []

	for tup in sentence:
		# tup=get_tuple(line)

		# ignoring non-tuple sentences and factual sentences
		# if(tup==False or tup[1][0]=='['):
		# 	continue

		# breaking second clause into list of words and lemmatizing
		verbWords = tup[1].lower().split(" ")
		lemWords = []
		for i in range(len(verbWords)):
			try:
				lemWords.append(lem.lemmatize(verbWords[i],'v'))
			except Exception as e:
				continue
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
			if(l>=3 and not( (word[l-2]=='l' and word[l-1]=='y') or (word in stopWords) )):
				# print word,
				rootVerbs.append(word)
			i+=1

	return rootVerbs

# breaks a string at prepositions and returns the list of clauses except the first clause.
def prep_break(s):
	delimiters = ["into","in","on","at","near","under","around","along"]

	# preprocessing the sentence
	s=s.replace(',','')
	s=s.lower()
	# to remove full stop at the end of sentence
	# if(s[-1]=='.'):
	# 	s=s[:-1]

	alongWithMarker="xcode1awx"
	s=s.replace("along with", alongWithMarker);

	# replacing prepositions by a delimiter
	token="xdelimx"
	for i in delimiters:
		delim=" "+i+" "
		s=s.replace(delim,token)
		delim=i+" "
		if(s[:len(delim)]==delim):
			l=list(s)
			l[:len(delim)]=list(token)
			s=''.join(l)

	s=s.replace(alongWithMarker, "along with");

	l=s.split("xdelimx")
	return l[1:]

# infile="july2017/july_openie_output.txt"
# txtOutfile="july2017/july_sent_selected.txt"
# jsonOutfile="july2017/july_sent_selected.json"

infile="july2017/july_openie_output.txt"
txtOutfile="july2017/july_sent_selected_casualty.txt"
jsonOutfile="july2017/july_sent_selected_casualty.json"

# whether or not to print the tuples of openie output
printOpenieTuples = False

file_object = open(infile,"r")
# month = file_object.read()
# month = json.loads(month)

lines = file_object.readlines()
file_object.close()

# set of verbs that indicate if sentence is to be selected
# keyVerbs = ["kill","injure","die","hit","ram","travel","say","occur","suffer","overturn","crash","fell","collide","return","sustain","carry","lose","happen","run","head","turn","crush","succumb","smash"]

keyVerbs1 = ["kill","die","succumb"]
# score1 = 3

keyVerbs2 = ["suffer","sustain","injure","hurt"]
# score2 = 2

# keyVerbs3 = ["say","travel","head","succumb"]
# score3 = 1

maxSentFromArticle = 3
sentence=[]
score=[]
article=[]
selectedSentences=[]
day=[]
month=[]

for line in lines:
	if(line[0]=='-'):

		if(len(sentence)>0):
			selectedTuples=[]
			for tup in sentence[1:]:
				rootVerbs=root_verbs([tup])
				inter1=intersection(rootVerbs,keyVerbs1)
				inter2=intersection(rootVerbs,keyVerbs2)
				if(len(inter1)>0 or len(inter2)>0):
					selectedTuples.append(tup[0])
			if(len(selectedTuples)>0):
				selectedTuples=list(set(selectedTuples))	# to remove duplicates
				article.append(selectedTuples)
				selectedTuples=[]
			sentence=[]

	elif(line[0]=='='):
		# usedIndices=[]
		# if(len(article)<=maxSentFromArticle):
		# 	selectedSentences=article
		# else:
		# 	tookPlaceFlag = False
		# 	for iter in range(maxSentFromArticle):
		# 		max = -sys.maxint - 1
		# 		for i in range(len(score)):
		# 			if(i in usedIndices):
		# 				continue
		# 			elif(max<score[i]):
		# 				max=score[i]
		# 				maxIndex=i
		# 		if(max==0):
		# 			break 	# not selecting sentences with score<=0
		# 		elif(max==sys.maxint and tookPlaceFlag==False):
		# 			tookPlaceFlag=True
		# 			usedIndices.append(maxIndex)
		# 			# print len(article), maxIndex
		# 			selectedSentences.append(article[maxIndex])
		# 		elif(max!=sys.maxint):
		# 			usedIndices.append(maxIndex)
		# 			# print len(article), maxIndex
		# 			selectedSentences.append(article[maxIndex])
		# 		else:
		# 			usedIndices.append(maxIndex)
		# 			# when max=sys.maxint and tookPlaceFlag=True then just add maxIndex to usedIndices


		# day.append(selectedSentences)
		day.append(article)
		article=[]
		# selectedSentences=[]
		# score=[]
		# should not be reqd but adding it as sometimes openIE output is not as expected.
		sentence=[]
	elif(line[0]=='+'):
		month.append(day)
		day=[]
		# should not be reqd but adding it as sometimes openIE output is not as expected.
		article=[]
		sentence=[]
		selectedSentences=[]
		score=[]

	elif(line[0]!='\n'):
		tup=get_tuple(line)
		if(tup!=False and tup[1][0]!='['):
			sentence.append(tup)
		else:
			sentence.append(line[:-1])	# to remove \n at end of line


# FOR TXT OUTPUT
file_object = open(txtOutfile,"w")
file_object.close()

file_object = open(txtOutfile,"a")
for day in month:
	for article in day:
		for sentence in article:
			for line in sentence:
				file_object.write(str(line)+"\n")
			# file_object.write(str(sentence[0])+"\n\n")
			# l=sentence[-1]
			# file_object.write(str(l[1:])+"\n")
			# file_object.write("\n---------------\n\n")
		file_object.write("====================\n\n")
	file_object.write("++++++++++++++++++++++++\n\n")
file_object.close()


# FOR JSON OUTPUT
with open(jsonOutfile, 'w+') as outfile:
    json.dump(month, outfile)

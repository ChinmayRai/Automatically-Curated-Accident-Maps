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
	if(not(s[0]=="0" and s[1]==".")):
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
			if(not( (word[l-2]=='l' and word[l-1]=='y') or (word in stopWords) )):
				# print word,
				rootVerbs.append(word)
			i+=1

	return rootVerbs


def prep_break(s):
	delimiters = ["into","in","on","at","near","under","around"]
	# along(!along with)
	s=s.replace(',','')
	token="xdelimx"
	for i in delimiters:
		delim=" "+i+" "
		s=s.replace(delim,token)
		delim=i+" "
		if(s[:len(delim)]==delim):
			l=list(s)
			l[:len(delim)]=list(token)
			s=''.join(l)

	l=s.split("xdelimx")
	return l[1:]


file_object = open(r"july2017/july_openie_output.txt","r")
# month = file_object.read()
# month = json.loads(month)

lines = file_object.readlines()
file_object.close()

# set of verbs that indicate if sentence is to be selected
# keyVerbs = ["kill","injure","die","hit","ram","travel","say","occur","suffer","overturn","crash","fell","collide","return","sustain","carry","lose","happen","run","head","turn","crush","succumb","smash"]

keyVerbs1 = ["kill","injure","die","hit","ram","occur","dash","overturn","crash","fell","fall","collide","happen","run","plunge","crush","mow","skid","knock","smash","tumble","topple","turn","plough","plow","cram","hurt"]
score1 = 3

keyVerbs2 = ["suffer","sustain","lose","end"]
score2 = 2

keyVerbs3 = ["say","travel","head","succumb"]
score3 = 1

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

			flag=False
			for t in sentence[1:]:
				# t=get_tuple(i)
				# if(t!=False):
				if(t[1]=="took" and t[2]=="place"):
					flag=True
				elif(t[1]=="met" and t[2][:4]=="with"):
					flag=True

			# rootVerbs = extract(sentence)
			rootVerbs=root_verbs(sentence[1:])
			
			if(flag):
				# assigning max score to this sentence so that it is always taken unless there are more than maxSentFromArticle number of such sentences
				score.append(sys.maxint)
			else:
				currScore = 0

				inter1=intersection(rootVerbs,keyVerbs1)
				inter2=intersection(rootVerbs,keyVerbs2)
				inter3=intersection(rootVerbs,keyVerbs3)
				
				currScore += len(inter1)*score1
				currScore += len(inter2)*score2
				currScore += len(inter3)*score3
				l=len(inter1)+len(inter2)+len(inter3)
				if(l):
					currScore /= l

				score.append(currScore)

			# sentence.append(rootVerbs)
			for i in range(len(sentence[1:])):
				index=1+i
				d=dict()
				d['tuple']=sentence[index]
				for cl in sentence[index]:
					if(cl[:2]=="L:"):
						d['L']=cl[2:]
					if(cl[:2]=="T:"):
						d['T']=cl[2:]
				sentence[index]=d

			posSentence=[]
			posSentence.append(prep_break(sentence[0]))
			for tup in sentence[1:]:
				s="".join(tup['tuple'][2:])
				s=s.replace("T:","")
				s=s.replace("L:","")
				
				l=prep_break(s)
				if(l!=[]):
					posSentence.append(l)

				# try:
				# 	s="".join(tup['tuple'][2:])
				# 	posSentence.append(prep_break(s))
				# except Exception as e:
				# 	print e
				# 	print tup['tuple']
			# sentence.append(posSentence)
			
			article.append(sentence+posSentence)
			

			# to print intersection of root verbs with key verbs
			# if(not(flag)):
			# 	rv=set()
			# 	for i in inter1:
			# 		rv.add(i)
			# 	for i in inter2:
			# 		rv.add(i)
			# 	for i in inter3:
			# 		rv.add(i)
			# 	article.append([list(rv)])
			sentence=[]

	elif(line[0]=='='):
		usedIndices=[]
		if(len(article)<=maxSentFromArticle):
			selectedSentences=article
		else:
			for iter in range(maxSentFromArticle):
				max = -sys.maxint - 1
				for i in range(len(score)):
					if(i in usedIndices):
						continue
					elif(max<score[i]):
						max=score[i]
						maxIndex=i
				usedIndices.append(maxIndex)
				# print len(article), maxIndex
				selectedSentences.append(article[maxIndex])

		day.append(selectedSentences)
		article=[]
		selectedSentences=[]
		score=[]
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
file_object = open("july2017/july_sent_selected.txt","w")
file_object.close()

file_object = open("july2017/july_sent_selected.txt","a")
for day in month:
	for article in day:
		for sentence in article:
			for line in sentence:
				file_object.write(str(line)+"\n")
			# file_object.write(str(sentence[0])+"\n\n")
			# l=sentence[-1]
			# file_object.write(str(l[1:])+"\n")
			file_object.write("\n---------------\n\n")
		file_object.write("====================\n\n")
	file_object.write("++++++++++++++++++++++++\n\n")
file_object.close()


# FOR JSON OUTPUT
with open('july2017/july_sent_selected.json', 'w+') as outfile:
# with open('july2017/july_sent_selected.json', 'w+') as outfile:
    json.dump(month, outfile)

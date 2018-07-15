import json
import sys
from root_verb_extractor import extract

# returns true if there are common elements in the 2 lists
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
	while(s[i]==" "):
		i+=1
	l=len(s)-1
	while(s[l]==" "):
		l-=1

	return s[i:l+1]

# converts openie output sentence to tuple
def get_tuple(s):
	if(not(s[0]=="0" and s[1]==".")):
		return False
	tup=s[5:]
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


# file_object = open(r"5day_5articles/july_sent_output.txt","r")
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
			for i in sentence:
				t=get_tuple(i)
				if(t!=False):
					if(t[1]=="took" and t[2]=="place"):
						flag=True
					elif(t[1]=="met" and t[2][:4]=="with"):
						flag=True
			if(flag):
				# assigning max score to this sentence so that it is always taken unless there are more than maxSentFromArticle number of such sentences
				score.append(sys.maxint)
			else:
				rootVerbs = extract(sentence)
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

			article.append(sentence)
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
		sentence.append(line)


with open('july2017/july_sent_selected.json', 'w+') as outfile:
    json.dump(month, outfile)

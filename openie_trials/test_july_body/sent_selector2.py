import json
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


file_object = open(r"5day_5articles/july_sent_output.txt","r")
# file_object = open(r"full_july/july_openie_output.txt","r")
# month = file_object.read()
# month = json.loads(month)

lines = file_object.readlines()
file_object.close()

# set of verbs that indicate if sentence is to be selected

# keyVerbs = ["kill","injure","die","hit","ram","travel","say","occur","suffer","overturn","crash","fell","collide","return","sustain","carry","lose","happen","run","head","turn","crush","succumb","smash"]

keyVerbs1 = ["kill","injure","die","hit","ram","occur","overturn","crash","fell","collide","happen","run","plunge","crush","mow","skid","knock","smash","tumble","topple","turn","plough","plow","cram","hurt"]

keyVerbs2 = ["suffer","sustain","lose","succumb"]

keyVerbs3 = ["say","travel","head"]


maxSentFromArticle = 2
sentence=[]
article=[]
day=[]
month=[]

for line in lines:
	if(line[0]=='-'):
		if(len(sentence)>0):
			rootVerbs = extract(sentence)

			inter1=intersection(rootVerbs,keyVerbs1)
			inter2=intersection(rootVerbs,keyVerbs2)
			inter3=intersection(rootVerbs,keyVerbs3)
			
			if(len(inter1)>0):
				sentence.append(inter1)
				article.append(sentence)

			elif(len(article)<maxSentFromArticle and len(inter2)>0):
				sentence.append(inter2)
				article.append(sentence)

			elif(len(article)<maxSentFromArticle and len(inter3)>0):
				sentence.append(inter3)
				article.append(sentence)			

			# for verb in rootVerbs:
			# 	if(verb in keyVerbs):
			# 		article.append(sentence)
			# 		break

			sentence=[]

	elif(line[0]=='='):
		day.append(article)
		article=[]
	elif(line[0]=='+'):
		month.append(day)
		day=[]

	elif(line[0]!='\n'):
		sentence.append(line)


with open('5day_5articles/july_sent_selected_multiList.json', 'w+') as outfile:
    json.dump(month, outfile)

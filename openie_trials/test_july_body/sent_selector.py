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
keyVerbs = ["kill","injure","die","hit","ram","travel","say","occur","suffer","overturn","crash","fell","collide","return","sustain","carry","lose","happen","run","head","turn","crush","succumb","smash"]

sentence=[]
article=[]
day=[]
month=[]

for line in lines:
	if(line[0]=='-'):
		if(len(sentence)>0):
			rootVerbs = extract(sentence)

			inter=intersection(rootVerbs,keyVerbs)
			if(len(inter)>0):
				sentence.append(inter)
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


with open('5day_5articles/july_sent_selected1.json', 'w+') as outfile:
    json.dump(month, outfile)

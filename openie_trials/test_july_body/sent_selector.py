import json
from root_verb_extractor import extract

file_object = open(r"july_sent_output.txt","r")
# month = file_object.read()
# month = json.loads(month)

lines = file_object.readlines()
file_object.close()

keyVerbs = ["kill","injure","die","hit","ram","travel","say","occur","suffer","overturn","crash","fell","collide","return","sustain","carry","lose","happen","run","head","turn","crush","succumb","smash"]

sentence=[]
article=[]
day=[]
month=[]

for line in lines:
	if(line[0]=='-'):
		if(len(sentence)>0):
			rootVerbs = extract(sentence)

			for verb in rootVerbs:
				if(verb in keyVerbs):
					article.append(sentence)

			sentence=[]

	elif(line[0]=="="):
		day.append(article)
	elif(line[0]=='+'):
		month.append(day)

	else:
		sentence.append(line)

# print month

with open('july_sent_selected.json', 'w+') as outfile:
    json.dump(month, outfile)

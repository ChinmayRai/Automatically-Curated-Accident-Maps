import json

def remove_newlines(s):
	s2 = ""
	for i in range(len(s)):
		if(s[i]=='\n'):
			i+=1
		else:
			s2 += s[i]
			i+=1
	return s2



file_object = open(r"output.json","r")
body = file_object.read()
j = json.loads(body)
file_object.close()

l=[]
for i in j:
	lines = i['lines']
	if(len(lines)>0):
		l.append(lines)

body = ['']*len(l)

for i in range(len(l)):
	s = ""
	for line in l[i]:
		s += line
	body[i] = remove_newlines(s)

# for i in body:
# 	print i

data = {"body" : body}

jsonData = json.dumps(data)
# print jsonData

with open('paragraphs.json','w') as f:
	json.dump(jsonData,f)

# file_object = open("paragraphs.json","w")
# file_object.write(json.dumps(data,ensure_acsii=False))
# file_object.close()
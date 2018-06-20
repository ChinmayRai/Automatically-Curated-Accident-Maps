import json

def add_links(lines,links):
	i=0;
	s=""
	for line in lines:
		s += line
		if(len(links)>i and line[len(line)-1]!='\n'):
			s+=links[i]
			i+=1

	return s 


def remove_newlines(s):
	# s=""
	# for line in l:
	# 	s += line
		
	s2 = ""
	for i in range(len(s)):
		if(s[i]=='\n'):
			i+=1
		else:
			s2 += s[i]
			i+=1
	return s2


# def remove_newlines(s):
# 	s2 = ""
# 	for i in range(len(s)):
# 		if(s[i]=='\n'):
# 			i+=1
# 		else:
# 			s2 += s[i]
# 			i+=1
# 	return s2



# file_object = open(r"output.json","r")
# body = file_object.read()
# j = json.loads(body)
# file_object.close()

# l=[]
# for i in j:
# 	lines = i['lines']
# 	if(len(lines)>0):
# 		l.append(lines)

# body = ['']*len(l)

# for i in range(len(l)):
# 	s = ""
# 	for line in l[i]:
# 		s += line
# 	body[i] = remove_newlines(s)

# data = {"body" : body}

# jsonData = json.dumps(data)

# with open('paragraphs.json','w') as f:
# 	json.dump(jsonData,f)


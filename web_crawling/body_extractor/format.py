import json

# def filter(s):
# 	s2 = ""
# 	for i in s:
# 		if(s[i]=='\n')
# 			i+=1
# 			continue
# 		else if(s[i]==' ' and i+1<len(s) and s[i+1])
# 			if(i+1==len(s))




file_object = open(r"output.json","r")
body = file_object.read()
j = json.loads(body)
file_object.close()

l=[]
for i in j:
	l.append(i['lines'])

q = l[1]
# print q


s = ""
for i in q:
	s += i

print s

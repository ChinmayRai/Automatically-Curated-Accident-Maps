import json
# j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
# print j['two']

file_object = open(r"positive_examples_titles.json","r")
titles = file_object.read()
j = json.loads(titles)
# print j
# print j[0]['title']

l=[]
for i in j:
	l.append(i['title'])

# uncomment to print the list
# for i in l:
# 	print i

file_object.close()

import json
# j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
# print j['two']

file_object = open(r"headings.json","r")
headings = file_object.read()
j = json.loads(headings)
# print j[0]['title']

l=[]
for i in j[0]['title']:
	l.append(i)

# uncomment to print the list
# for i in l:
# 	print i

file_object.close()

# d=dict()
# print "initial dictionary"
# print d
# print "\n"

# d[0]=123
# d['asd']="wad"
# x=4
# d[x]=12

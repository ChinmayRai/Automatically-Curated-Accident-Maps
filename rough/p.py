import json
# j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
# print j['two']

file_object = open(r"headings.json","r")
headings = file_object.read()
j = json.loads(headings)
# print j[0]['title']

d=dict()
print d

d[0]=123
# d['asd']="wad"
print d

# for i in j[0]['title']:
#  	d['heading'][i] = j[0]['title'][i]
#  	d['label'][i] = 0


file_object.close()
import json


inFile="formated_for_mapping.json"
jsonOutfile="formated_for_mapping.json"


file_object = open(inFile,"r")
locations = file_object.read()
locations = json.loads(locations)
file_object.close()


def find(s):
	l = ['bypass','nh','highway','corridor','road','expressway']
	for w in l:
		if s.find(w)>=0:
			return true
	return false



list = locations['features']

for article in list:
	add=[]
	road=[]
	for address in article['properties']['Address']:
		if find(address):
			road.add(address)
		else if address.find('way to')==-1:
			add.add(address)
	article['properties']['Address']=add
	article['properties']['Road']=road


file_object = open(jsonOutfile,"w+")
file_object.close()

with open(jsonOutfile, 'w+') as outfile:
    json.dump(coordinates, outfile)	

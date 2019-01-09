import json


inFile="formatted_for_mapping.json"
jsonOutfile="data.json"


file_object = open(inFile,"r")
locations = file_object.read()
locations = json.loads(locations)
file_object.close()


def find(s):
	l = ['bypass','nh','highway','corridor','road','expressway']
	for w in l:
		if s.find(w)>=0:
			return True
	return False



lis = locations['features']

for article in lis:
	add=[]
	road=[]
	for address in article['properties']['Address']:
		if find(address):
			road.append(address)
		elif address.find('way to')==-1:
			add.append(address)
	article['properties']['Address']=add
	article['properties']['Road']=road

locations['features'] = lis

file_object = open(jsonOutfile,"w+")
file_object.close()

with open(jsonOutfile, 'w+') as outfile:
    json.dump(locations, outfile)	

import requests
import json


inFile="location.json"
jsonOutfile="coordinates.json"


file_object = open(inFile,"r")
locations = file_object.read()
locations = json.loads(locations)
file_object.close()

coordinates=[]
API_KEY="AIzaSyDx3cH2CoYlfM-Z1p8cHKYGrkXpqRIBMpc"
#"AIzaSyABji3II-_zS0WWLrDvCvU5zrfsw3IX9_0"

for i in locations:
	l=i['loc']
	l=l.replace(' ','+')
	
	# l=locations[0]['loc']
	# l=l.replace(' ','+')
	# print l

	url="https://maps.googleapis.com/maps/api/geocode/json?address="+l+"&key="+API_KEY
	try:
		r = requests.get(url)
		coor=r.json()['results'][0]['geometry']['location']
		coordinates.append(coor)
	except Exception:
		print r.status_code
		print i

file_object = open(jsonOutfile,"w+")
file_object.close()

with open(jsonOutfile, 'w+') as outfile:
    json.dump(coordinates, outfile)	
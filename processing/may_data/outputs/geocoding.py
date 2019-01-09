import json
import googlemaps
from datetime import datetime



inFile="data.json"
jsonOutfile="geojson.json"

file_object = open(inFile,"r")
file = file_object.read()
file = json.loads(file)
file_object.close()

lis = file['features']

gmaps = googlemaps.Client(key='AIzaSyDx3cH2CoYlfM-Z1p8cHKYGrkXpqRIBMpc')

for article in lis:
	loc = article['properties']['RepLoc']
	if (len(loc)+len(article['properties']['Address'])>0):
		d=0
		latlng ={}
		add=""
		if(len(article['properties']['Address'])>0):
			for address in article['properties']['Address']:
				r=gmaps.geocode(address.replace(' ','+')+', +'+loc)
				if r==[]:
					break
				depth = len(r[0]['address_components'])
				if (depth>d):
					d=depth
					latlng = r[0]['geometry']['location']
					add = r[0]['formatted_address']			
		else:
			r=gmaps.geocode(loc)
			latlng=r[0]['geometry']['location']
			add = r[0]['formatted_address']
		article['properties']['Address'] = add
		print(add)
		article['properties']['latlng']  = latlng


file['features'] = lis

file_object = open(jsonOutfile,"w+")
file_object.close()

with open(jsonOutfile, 'w+') as outfile:
    json.dump(file, outfile)	

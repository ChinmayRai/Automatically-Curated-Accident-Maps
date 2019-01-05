# DESCRIPTION : gets location, time, no. of casualties from different files and formats them into a single file according to the format required by mapbox plotting

import json

bodyFile = "article_body.json"
numCasualtyFile = "num_casualty.json"
timeFile = "time.json"
locationFile = "prop_noun_clauses.json"
jsonOutfile = "formatted_for_mapping.json"

# READING INPUT
file_object = open(bodyFile,"r")
body = file_object.read()
body = json.loads(body)
file_object.close()

file_object = open(numCasualtyFile,"r")
numCasualty = file_object.read()
numCasualty = json.loads(numCasualty)
file_object.close()

file_object = open(timeFile,"r")
timeClause = file_object.read()
timeClause = json.loads(timeClause)
file_object.close()

file_object = open(locationFile,"r")
location = file_object.read()
location = json.loads(location)
file_object.close()

# COMBINING
# concatinating all time clauses
timeStr=""
for t in timeClause[-1]:
	timeStr+=t+", "
timeStr=timeStr[:-2]

# combining all locations into a single list
locArray=[]
for l in location:
	locArray+=l[-1]



geojson = dict()
geojson['type'] = "FeatureCollection"
geojson['features'] = []

n=1
for j in range(n):
	add = locArray
	Casualty = numCasualty
	repLoc = body["repLoc"]
	time = timeStr

	newFeature = {
	"type": "Feature","geometry": {"type": "Point"},
	"properties": {"Address": add, "Time": time, "RepLoc": repLoc, "Casualty": Casualty }
	}
	geojson['features'].append(newFeature);


# JSON OUTPUT
with open(jsonOutfile, 'w+') as outfile:
    json.dump(geojson, outfile)
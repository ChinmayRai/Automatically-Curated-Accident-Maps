# DESCRIPTION : top level function that processes entire month's data
# input - openie output of month, raw body in json
# output - features formatted for mapping

import json
import os
from formater import format

bodyFile="inputs/may_2017_output.json"
openieOutputFile="inputs/may_openie_output.txt"
tempArticleOpenieOutputFile="temp_files/article_openie_output.txt"
tempArticleBodyFile="temp_files/article_body.json"
outFile="outputs/formated_for_mapping.json"

file_object = open(openieOutputFile,"r")
lines = file_object.readlines()
file_object.close()

file_object = open(bodyFile,"r")
month = file_object.read()
month = json.loads(month)
file_object.close()

startLine=0
endLine=0

date=0
mon=5
year=2017

geojson = dict()
geojson['type'] = "FeatureCollection"
geojson['features'] = []

for d in range(len(month)):
	day=month[d]
	date=d+1
	for a in range(len(day)):
		article=day[a]
		
		print "day="+str(d)+" article="+str(a)

		# getting openie output of a single article
		startLine=endLine
		while(lines[endLine][0]!="="):
			endLine+=1
		endLine+=1
		openieOutput=lines[startLine:endLine]

		# writing openie output of single article to file
		file_object = open(tempArticleOpenieOutputFile,"w")
		for line in openieOutput:
			file_object.write(line)
		file_object.close()

		# writing body of a single article to a file
		with open(tempArticleBodyFile, 'w+') as outfile:
		    json.dump(article, outfile)

	    # running pipeline for a single article
		command="./run_single_article.sh "+str(date)+" "+str(mon)+" "+str(year)
		os.system(command)

		# formating outputs from different files into a single data structure
		newFeature=format()
		geojson['features'].append(newFeature);

		# break

	while(lines[endLine][0]!="+"):
		endLine+=1
	endLine+=1

	# break

# JSON OUTPUT
with open(outFile, 'w+') as outfile:
	json.dump(geojson, outfile)









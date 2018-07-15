import json

file_object = open(r"july2017/july_2017_sent_token.json","r")
month = file_object.read()
month = json.loads(month)
file_object.close()

output=""

for day in month:
	for article in day:
		for line in article['body']:
			output+=line
			output+=" -----------. "	# line end
		output+=" ============. "		# article end
	output+=" +++++++++++++++++++. "	# day end
output+=" //////////////. "				# month end
# to remove error due to \u2018
output = output.encode('utf-8')

# print output
file_object = open(r"july2017/july_sent.txt","w")
file_object.write(output)
file_object.close()


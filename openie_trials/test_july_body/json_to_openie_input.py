import json

file_object = open(r"july_2017_output.json","r")
month = file_object.read()
month = json.loads(month)
file_object.close()

output=""

for day in month:
	for article in day:
		output+=article['body']
		output+=" ------------------------. "
	output+=" +++++++++++++++++++++++++++++. "

# to remove error due to \u2018
output = output.encode('utf-8')

# print output
file_object = open(r"july_body.txt","w")
file_object.write(output)
file_object.close()


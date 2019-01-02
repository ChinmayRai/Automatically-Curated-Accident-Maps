import json
from cleaner import clean

# file_object = open(r"5day_5articles/july_2017_sent_token.json","r"))
infile="article_sent_token.json"
outfile="article_openie_input.txt"

file_object = open(infile,"r")
article = file_object.read()
article = json.loads(article)
file_object.close()

output=""

# for day in month:
	# for article in day:
for line in article['body']:
	try:
		output+=clean(line)
	except Exception as e:
		print e
		print "while cleaning ==="+line+"=== end"

	output+=" -----------. "	# line end
output+=" ============. "		# article end
	# output+=" +++++++++++++++++++. "	# day end
# output+=" //////////////. "				# month end
# to remove error due to \u2018
output = output.encode('utf-8')

# print output
file_object = open(outfile,"w")
# file_object = open(r"5day_5articles/july_sent.txt","w")
file_object.write(output)
file_object.close()


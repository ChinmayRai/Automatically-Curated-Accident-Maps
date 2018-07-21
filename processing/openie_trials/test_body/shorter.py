import json

file_object = open(r"july_2017_sent_token.json","r")
month = file_object.read()
month = json.loads(month)
file_object.close()

month=month[:5]
for i in range(len(month)):
	month[i]=month[i][:5]

# to remove error due to \u2018
# month = output.encode('utf-8')

print month

with open('july_2017_sent_token.json', 'w+') as outfile:
    json.dump(month, outfile)

# file_object = open(r"july_2017_sent_token.txt","w")
# file_object.write(month)
# file_object.close()

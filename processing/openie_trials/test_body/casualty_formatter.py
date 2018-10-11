import json
import operator

infile="july2017/july_sent_selected_casualty.json"
txtOutfile="july2017/july_casualty_formated.txt"
jsonOutfile="july2017/july_casualty_formated.json"

file_object = open(infile,"r")
month = file_object.read()
month = json.loads(month)

# flattening lists of lists of lists to a single list
month = sum(sum(sum(month,[]),[]),[])

frequency=dict()
for i in month:
	i=i.lower()
	if i in frequency:
		frequency[i]+=1
	else:
		frequency[i]=1
#sorted_freq is list of all subjects in decreasing order of their frequency
sorted_freq = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
# print sorted_freq


# FOR TXT OUTPUT
file_object = open(txtOutfile,"w")
file_object.close()

file_object = open(txtOutfile,"a")
for i in sorted_freq:
	file_object.write(str(frequency[i[0]])+ "\t" + i[0] + "\n")
	

# FOR JSON OUTPUT
with open(jsonOutfile, 'w+') as outfile:
    json.dump(sorted_freq, outfile)
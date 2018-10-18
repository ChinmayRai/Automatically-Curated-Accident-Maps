import json
from num_casualty import num_casualty

infile="july_casualty_formated.json"
txtOutfile="july_num_casualty.txt"
# jsonOutfile="july_num_casualty.json"

file_object = open(infile,"r")
month = file_object.read()
month = json.loads(month)

# for i in range(len(month)):
#     print(month[i][0])
#     print num_casualty(month[i][0])


# FOR TXT OUTPUT
file_object = open(txtOutfile,"w")
file_object.close()

file_object = open(txtOutfile,"a")
count=0
for i in range(len(month)):
	file_object.write(month[i][0] + "\n")
	num=num_casualty(month[i][0])
	if(num!=[]):
		file_object.write(str(num[0]) + "\n")
	else:
		file_object.write("----- \n")
	if(num==[]):
		count=count+1

# print(len(month))
# print count

# # FOR JSON OUTPUT
# with open(jsonOutfile, 'w+') as outfile:
#     json.dump(sorted_freq, outfile)
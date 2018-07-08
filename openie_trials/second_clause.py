
# file_object = open(r"out.txt","r")
file_object = open(r"May_2017_IE.txt","r")
# month = file_object.read()
# month = json.loads(month)

lines = file_object.readlines()
file_object.close()

for line in (lines):
	if(line[0]=='0' and line[1]=='.'):
		# print (line)
		verb = ""
		i=0
		while(line[i]!=";"):
			i+=1
		i+=2;
		while(line[i]!=";"):
			verb += line[i]
			i+=1

		print (verb)
# from sent_selector5 import get_tuple

# removes extra spaces from edges of string
def trim(s):
	i=0
	while(s[i]==" "):
		i+=1
	l=len(s)-1
	while(s[l]==" "):
		l-=1

	return s[i:l+1]

def get_tuple(s):
	if(not(s[0]=="0" and s[1]==".")):
		return False
	print s
	print s[5:]
	print s[5:-1]
	tup=s[5:-1]	# -1 to remove \n from the end
	if(tup[0]=="("):
		tup=tup[1:-1]
	elif(tup[:7]=="Context"):
		i=0
		while(tup[i]!=":"):
			i+=1
		tup=tup[i+2:-1]

	arr=tup.split(";")

	for i in range(len(arr)):
		arr[i]=trim(arr[i])

	return tuple(arr)

s="0.92 (Ashok Kondiba Thakur; was killed; T:after the car)\n"


# print get_tuple(s)
sentence=[('he', 'was travelling', 'in crashed into the barricades along BRTS (Bus Rapid Transit System) route in Akurdi'), ('Ashok Kondiba Thakur', 'was killed', 'T:after the car')]

print sentence
for i in range(len(sentence)):
	d=dict()
	d['tuple']=sentence[i]
	for cl in sentence[i]:
		if(cl[:2]=="L:"):
			d['L']=cl[2:]
		if(cl[:2]=="T:"):
			d['T']=cl[2:]
	sentence[i]=d

print
print sentence
print "============"

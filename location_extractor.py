from nltk.tag import StanfordNERTagger
import sys
import json
import time

start = time.time()


def loc(text):
	st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz') 
	k=(st.tag(text.split()))
	l=[]
	for i in k:
		if(i[1]=='LOCATION'):
			l.append(i[0])
	return l

file=sys.argv[1]
file_object = open(file,"r")
s = file_object.read()
s = json.loads(s)
file_object.close()

month =[]
for date in range(len(s)):
	day = []
	for k in s[date]:
		d = dict()
		d['title'] = k['title']
		d['body'] =  k['body']
		d['locations']= loc(k['body'])
		day.append(d)

	print "day " + str(date+1) + " over"
	month.append(day)

with open('june_2017_loc.json', 'w+') as outfile:
    json.dump(month, outfile)

end = time.time()
print "total time = " + str(round(end - start,2)) + " sec"
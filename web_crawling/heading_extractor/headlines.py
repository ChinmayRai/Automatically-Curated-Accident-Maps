import os
import json

def extract(s):
	# shell_command = 'scrapy runspider headings_spider.py -a ip=\"'
	# shell_command += s
	# shell_command += '\" -o headlines.json'

	# print shell_command
	# print "=============================================================================="

	# os.system(shell_command)

	file_object = open(r"headlines.json","r")
	heads = file_object.read()
	j = json.loads(heads)
	file_object.close()

	# print len(j[0]['title'])
	# print j[0]['url']
	# print j[0]['title']
	

	l=[]
	length = len(j[0]['url'])
	for i in range(length):
		d = dict()
		d['url'] = j[0]['url'][i]
		d['title'] = j[0]['title'][i]

		if(d['title']):
			l.append(d)

	return l

# os.system('scrapy runspider sp.py -a ip="2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms" -o a.json')
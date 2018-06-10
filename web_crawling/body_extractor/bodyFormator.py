import os
import json

def extract(s):
	shell_command = 'scrapy runspider body_spider.py --nolog -a ip=\"'
	shell_command += s
	shell_command += '\" -o body.json'

	print shell_command
	print "=============================================================================="

	# file_object = open("body.json","w+").close
	# os.system(shell_command)

	file_object = open(r"body.json","r")
	body = file_object.read()

	try:
		j = json.loads(body)
		return j[0]
	except ValueError as e:
		print e
		print body
		print "================"


	# j = json.loads(body)
	# return j[0]

	file_object.close()

	# print len(j[0]['title'])
	# print j[0]['url']
	# print j[0]['title']
	

# uncomment if you want array of dictionaries where each dictionary has 'url' and 'title'
	# l=[]
	# length = len(j[0]['url'])
	# for i in range(length):
	# 	d = dict()
	# 	d['url'] = j[0]['url'][i]
	# 	d['title'] = j[0]['title'][i]

	# 	if(d['title']):
	# 		l.append(d)

	# return l

# os.system('scrapy runspider sp.py -a ip="2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms" -o a.json')
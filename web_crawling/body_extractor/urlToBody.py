import bodyFormator
import format
import json
import time

start = time.time()

file_object = open(r"july_2017.json","r")
urls = file_object.read()
urls = json.loads(urls)
file_object.close()

# query = "https://timesofindia.indiatimes.com/city/amritsar/gurdaspur-man-dies-in-accident-in-saudi-firm/articleshow/63979282.cms?"
# b = bodyFormator.extract(query)

month =[]
for date in range(len(urls)):
	day = []
	for url in urls[date]:
		b = bodyFormator.extract(url)
		if (b!={} and b['lines']!=[]):
			d = dict()
			d['title'] = b['title']
			withLinks = z=format.add_links(b['lines'],b['links'])
			article = format.remove_newlines(withLinks)
			loc, article = format.reporting_location(article)
			d['repLoc'] = loc
			d['body'] = article
			day.append(d)

	print "day " + str(date) + " over"
	month.append(day)

# print "======month over"

# file_object = open(r"june_2017_output.json","w+")
# file_object.write(month)
# file_object.close()

with open('july_2017_output.json', 'w+') as outfile:
    json.dump(month, outfile)


end = time.time()
print "total time = " + str(round(end - start,2)) + " sec"
import headlines

# just add whatever comes after 'https://timesofindia.indiatimes.com/' in URL in a string
query = "2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms"
# and pass that string as a parameter to headlines.extract to recieve an array
d = headlines.extract(query)


# do whatever with that array now
# for i in range(5):
# 	print d['url'][i]
# 	print d['title'][i]
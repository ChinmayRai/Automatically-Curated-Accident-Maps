import headlines

query = "2018/5/26/archivelist/year-2018,month-5,starttime-43246.cms"
arr = headlines.extract(query)

for i in range(5):
	print arr[i]
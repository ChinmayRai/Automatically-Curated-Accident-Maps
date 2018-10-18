import re

# given string s, return list of tuples (number, word index) that appears in the string, returns empty list if no number is found
def num_casualty(s):
	s=s.replace('-',' ')
	# print s
	l=s.split(' ')
	ans=[]
	d={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'he':1,'she':1}
	for i in range(len(l)):
		foundNumber=False
		if(l[i].isdigit()):
			tup=tuple((int(l[i]),i))
			foundNumber=True
		elif(l[i] in d.keys()):
			tup=tuple((d[l[i]],i))
			foundNumber=True
		# exclude number if followed by 'year'
		if( foundNumber and not(i+1<len(l) and l[i+1]=="year") and not( i-1>=0 and l[i-1]=="," and i+1<len(l) and l[i+1]=="," )):
			ans.append(tup)
	return ans



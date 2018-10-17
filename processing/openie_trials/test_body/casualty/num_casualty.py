import re

# given string s, return list of tuples (number, word index) that appears in the string, returns empty list if no number is found
def num_casualty(s):
	s=s.replace('-',' ')
	# print s
	l=s.split(' ')
	ans=[]
	d={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10}
	for i in range(len(l)):
		if(l[i].isdigit()):
			ans.append(tuple((int(l[i]),i)))
		elif(l[i] in d.keys()):
			ans.append(tuple((d[l[i]],i)))
	return ans



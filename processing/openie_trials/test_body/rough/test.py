# breaks a string at prepositions and returns the list of clauses except the first clause.
def prep_break(s):
	delimiters = ["into","in","on","at","near","under","around","along"]

	# preprocessing the sentence
	s=s.replace(',','')
	s=s.lower()
	# to remove full stop at the end of sentence
	# if(s[-1]=='.'):
	# 	s=s[:-1]

	alongWithMarker="xcode1awx"
	s=s.replace("along with", alongWithMarker);

	# replacing prepositions by a delimiter
	token="xdelimx"
	for i in delimiters:
		delim=" "+i+" "
		s=s.replace(delim,token)
		delim=i+" "
		if(s[:len(delim)]==delim):
			l=list(s)
			l[:len(delim)]=list(token)
			s=''.join(l)

	s=s.replace(alongWithMarker, "along with");

	l=s.split("xdelimx")
	return l[1:]


s="According to police, Jevika was travelling with her parents in the same bus and had alighted near Ram Nagar in Bhatta Basti."
print s
print prep_break(s),'\n'

s="Near the banks of yamuna at night."
print s
# print list(s)
print prep_break(s),'\n'

s="He was walking along the banks of river Yamuna on Monday morning, savouring the tides along with the cool breeze."
print s
print prep_break(s),'\n'
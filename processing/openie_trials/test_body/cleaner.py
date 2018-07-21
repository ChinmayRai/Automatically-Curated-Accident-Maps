from nltk import word_tokenize, pos_tag

# removed redundant phrases to improve openie output
def clean(s):
	# the following phrases will be removed from the string
	phrases = ["in which they were travelling","on which they were travelling","in which the victims were travelling","in which the victims were riding","they were on","they were in"]
	for phrase in phrases:
		i=s.find(phrase)
		if(i!=-1):
			s=s[:i-1]+s[i+len(phrase):]	#i-1 is to delete a space on one side
	# this phrase will be removed only if the succeeding word is a verb
	phrase="they were travelling in"
	posVerbs=['VB','VBD','VBG','VBN','VBP','VBZ']
	i=s.find(phrase)
	if(i!=-1):
		if (s[i+len(phrase)]!=","):
			if(s[i+len(phrase)+1]==","):
				words=(s[i:i+len(phrase)]+", "+s[i+len(phrase)+3:]).split(" ")
			else :
				words=(s[i:i+len(phrase)]+", "+s[i+len(phrase)+1:]).split(" ")
		else :
			words=s[i:].split(" ")
		print(words)
		pos=pos_tag(words)
		print(pos)
		if(pos[4][1] in posVerbs):
			s=s[:i]+s[i+len(phrase):]
	return s
##"they were travelling on verb"
##"in which the t1 (t2)? were travelling"
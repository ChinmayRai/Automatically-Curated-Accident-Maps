from nltk import word_tokenize, pos_tag

# removed redundant phrases to improve openie output
def clean(s):
	# the following phrases will be removed from the string
	phrases = ["in which they were travelling","in which the victims were travelling","they were on"]
	for phrase in phrases:
		i=s.find(phrase)
		if(i!=-1):
			s=s[:i-1]+s[i+len(phrase):]	#i-1 is to delete a space on one side
	# this phrase will be removed only if the succeeding word is a verb
	phrase="they were travelling in "
	posVerbs=['VB','VBD','VBG','VBN','VBP','VBZ']
	i=s.find(phrase)
	if(i!=-1):
		words=s[i:].split(" ")
		pos=pos_tag(words)
		if(pos[4][1] in posVerbs):
			s=s[:i]+s[i+len(phrase):]
	return s

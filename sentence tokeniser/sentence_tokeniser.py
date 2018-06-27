# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize

def add_spaces(s):
	s2=""
	i=0
	l=len(s)
	# count=0	#to track how many spaces have been added
	for i in range(l):
		s2+=s[i];
		if(i<l-1 and s[i]=='.' and ord(s[i+1])>=65 and ord(s[i+1])<=90 ):
			s2+=" "
			# count+=1

	# print count
	return s2

def sentence_tokenise(para):
	para = add_spaces(para)
	sentences = sent_tokenize(para)

	return sentences

# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize

def add_spaces(s):
	s2=""
	i=0
	l=len(s)
	# count=0	#to track how many spaces have been added
	for i in range(l):
		s2+=s[i];
		if(i<l-1 and s[i]=='.' and ( (ord(s[i+1])>=65 and ord(s[i+1])<=90) or ord(s[i+1])==34 ) ):
			s2+=" "
			# count+=1

	# print count
	return s2

def replace(s):
	s=s.replace('Mr.', 'Mister')
	s=s.replace('No.', 'Number')
	s=s.replace('no.', 'number')
	return s

def sentence_tokenise(para):
	para = replace(para)
	para = add_spaces(para)
	sentences = sent_tokenize(para)

	return sentences

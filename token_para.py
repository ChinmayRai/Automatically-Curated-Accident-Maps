# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
 
data="this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn."
a=sent_tokenize(data)
for i in range(0,len(a)):
	print(a[i])
	print("\n")
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


para2="this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn."

para = "Ponda: Vithu Betkikar, 60, from Kulkarniwada in Betki, died on Friday morning when the scooter he was riding was hit by an oncoming car at Mardol, Ponda. Betkikar was proceeding towards Kundaim.Another scooterist, 32-year-old Maruti Polekar from Usgao, too, was knocked down in the accident and severely injured. He was rushed to the sub district hospital in Ponda, police said.The driver of the car, Suresh Biradar, 30, from Usgao, was arrested late Friday evening and booked for causing death, injury, and endangering lives due to rash and negligent driving."

para = add_spaces(para)
para2 = add_spaces(para2)

# print ("\n\n\n")

# a=sent_tokenize(para2)
# for i in range(0,len(a)):
# 	print(a[i])

# print("\n")

sentences = sent_tokenize(para)
print sentences
print ("\n")

for i in sentences:
	print i

# print ("\n")
# words = word_tokenize(para)
# print words	
# print ("\n")
# for i in words:
# 	print i


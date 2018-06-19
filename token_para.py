# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
 
data="this’s a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn."

body = "Ponda: Vithu Betkikar, 60, from Kulkarniwada in Betki, died on Friday morning when the scooter he was riding was hit by an oncoming car at Mardol, Ponda. Betkikar was proceeding towards Kundaim.Another scooterist, 32-year-old Maruti Polekar from Usgao, too, was knocked down in the accident and severely injured. He was rushed to the sub district hospital in Ponda, police said.The driver of the car, Suresh Biradar, 30, from Usgao, was arrested late Friday evening and booked for causing death, injury, and endangering lives due to rash and negligent driving."
a=sent_tokenize(data)
for i in range(0,len(a)):
	print(a[i])

print("\n")

b= sent_tokenize(body)
for i in b:
	print i
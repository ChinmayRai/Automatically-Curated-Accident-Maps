from nltk.tokenize import sent_tokenize, word_tokenize
from sentence_tokeniser import sentence_tokenise
import json


# para = "Ponda: Vithu Betkikar, 60, from Kulkarniwada in Betki, died on Friday morning when the scooter he was riding was hit by an oncoming car at Mardol, Ponda. Betkikar was proceeding towards Kundaim.Another scooterist, 32-year-old Maruti Polekar from Usgao, too, was knocked down in the accident and severely injured. He was rushed to the sub district hospital in Ponda, police said.The driver of the car, Suresh Biradar, 30, from Usgao, was arrested late Friday evening and booked for causing death, injury, and endangering lives due to rash and negligent driving."

# sentences = sentence_tokenise(para)

# print sentences
# print ("\n")

# for i in sentences:
# 	print i

infile="article_body.json"
jsonOutfile="article_sent_token.json"

file_object = open(infile,"r")
article = file_object.read()
article = json.loads(article)
file_object.close()


# print (body[1][0]['body'])

# for date in month:
	# for article in date:
para = article['body']

sentences = sentence_tokenise(para)
article['body'] = sentences
		# for s in sentences:
		# 	print s
		# print "after add_spaces = ",len(sentences)

		## without adding spaces
		# sentences = sent_tokenize(para)
		# for s in sentences:
		# 	print s
		# print "before add_spaces = ",len(sentences)


with open(jsonOutfile, 'w+') as outfile:
    json.dump(article, outfile)

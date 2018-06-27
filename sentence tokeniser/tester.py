from sentence_tokeniser import sentence_tokenise

para = "Ponda: Vithu Betkikar, 60, from Kulkarniwada in Betki, died on Friday morning when the scooter he was riding was hit by an oncoming car at Mardol, Ponda. Betkikar was proceeding towards Kundaim.Another scooterist, 32-year-old Maruti Polekar from Usgao, too, was knocked down in the accident and severely injured. He was rushed to the sub district hospital in Ponda, police said.The driver of the car, Suresh Biradar, 30, from Usgao, was arrested late Friday evening and booked for causing death, injury, and endangering lives due to rash and negligent driving."

sentences = sentence_tokenise(para)

print sentences
print ("\n")

for i in sentences:
	print i


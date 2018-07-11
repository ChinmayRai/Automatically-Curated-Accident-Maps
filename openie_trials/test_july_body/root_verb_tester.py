from root_verb_extractor import extract

l="Ashok Kondiba Thakur, a 61-year-old resident of Bopodi, was killed after the car he was travelling in crashed into the barricades along BRTS (Bus Rapid Transit System) route in Akurdi late on Wednesday night.\n0.61 (he; was travelling; in crashed into the barricades along BRTS (Bus Rapid Transit System) route in Akurdi)\n0.92 (Ashok Kondiba Thakur; was killed; T:after the car)\n-----------.".split('\n')

rootVerbs=extract(l)

print rootVerbs
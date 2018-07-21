# SURA

TO DO: 21/7
1) Exp with - diff weights of lists
			- adding list 0 containing only kill, die, injure
			- shuffling verbs amongst lists

2) start extracting loc, time, casualities from selected lists


Issues:
1. body output - may 2017 - day11, article 0 - body has numbers 1 to 6 in it.
2. sentence tokenizer made this split:
In another spine-chilling accident, a 20-year-old engineering student died after ramming his i20 into a road divider at high speed near Green Mosque on Road No.
3, Banjara Hills on Tuesday afternoon.

	=== soln - replace No. with number, Mr. with mister

3. we need to use the sentence selector to eliminate the negative examples of accidents news from the selected sentences. The negative examples tend to have few/no instances of verb which are important to us.

	=== remove sentence having score=0 or (score = some threshold)

4. limit the number of sentences that are marked relevant on basis of "took place" to 1.
	=== implement this



Negative Examples(May 2017):
1. Woman who lost kin in road accident made Swachh ambassador
2. Man claims his car was stolen on SG Road
3. On the road: Prevent a car blaze, get vehicle serviced at right place
4. 4-year-old girl maimed in truck mishap gets Rs 6 lakh compensation.
5. 200 killed in highway accidents in April alone
6. Hit by stray road rage bullet, 13-year-old Aligarh schoolgirl dies
7. Five-year-old girl dies inside locked car
8. Petrol pump staffer dies in accident
9. Retired colonel told to pay 14 lakh relief to accident victim's kin
10. HC raises relief to family of Vizag accident victim
11. Drunk crane driver falls into nala, dies
12. Chemical accident: 1 dead, 4 critical
13. Woman delivers healthy child after car crash left her limbs paralysed
14. Road cutting turns Kanpur Road into a stretch of pits
15. Coconut tree crashes into home, injures old lady
16. Hurt in bus shelter crash month before exam, she scores

	
# Postponed for fine-tuning afterwards:
For headline classification:
1. nonML approach accuracy test using ml approach training set
2.	Non ML Approach :
	1. Key word extraction
	2. Score Assignment
	3. Threshold guessing

for automation of pipeline
3. automate openie by Popen


scrapy runspider news.py -o article.json
scrapy runspider news.py -o article.jl

Difficult to predict positive example:
1. 25may:
"46-year-old cyclist dies in hit-and-run",


//to run stanford coreNlp
java -mx3g edu.stanford.nlp.naturalli.OpenIE -format ollie


OpenNLP :
for POS tagging - 
	./opennlp POSTagger ../en-pos-maxent.bin < sentence.txt

chunker example - 
https://www.tutorialkart.com/opennlp/chunker-example-in-apache-opennlp/

openNLP pretrained models - 
http://opennlp.sourceforge.net/models-1.5/



Access of internal server:
	riju@10.208.23.195
	riju


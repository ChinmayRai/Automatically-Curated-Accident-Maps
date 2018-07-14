# SURA

TO DO: 14/7 - Complete Sentence Selection and automated pipeline

	Samarth - 3 list model for sentence classification
			-  ." to . " in sent_tokeniser

	Chinmay - automate openie by Popen


Postponed:
	Samarth - 	2) run openNLP chunker, dont spend a lot of time
				3) try running GeoParsePy - no zada matha pachi
	Chinmay - 1) Read about text mining


how to filter out sentences on which to run NER - summarization tools filter out sentences containing facts

Issues:
1. body output - may 2017 - day11, article 0 - body has numbers 1 to 6 in it.
2. 

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
13.

	
Postponed for fine-tuning afterwards:
1. nonML approach accuracy test using ml approach training set
2.	Non ML Approach :
	1. Key word extraction
	2. Score Assignment
	3. Threshold guessing


scrapy runspider news.py -o article.json
scrapy runspider news.py -o article.jl


25may:
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


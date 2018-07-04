# SURA

TO DOs:

keshav mail - detailed mail, how to build our system, get advice,	ask about word shapes features
prachi mail - confirm meeting
mausam search 	- word shape, does stanNER has it
				- regarding indan NER datasets


3/7:
	Samarth - 	2) run openNLP chunker, dont spend a lot of time
				1) Google NLP on local machine - VV imp - first priority
				3) try running GeoParsePy - no zada matha pachi

	Chinmay - 1) Read about text mining


how to filter out sentences on which to run NER - summarization tools filter out sentences containing facts

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


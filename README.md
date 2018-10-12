# SURA

# TO DO: 12/10
1. No. of casualties - Work on inference engine
2. Testing - automate using fraction matched
3. Plotting - debug why geotagged to US
4.* Report - Complete Report


# Golden Set Evaluation & Observations :
Location : 
1. failures at "east of Moscow"
2. location is not detected as noun thereby gets rejected
3. add 'of' to prepositions - at many places we have <so and so place> of <so and so area>
4. add 'ahead' to preposition list - eg. "According to police, the accident occurred ahead of the NSG camp gate on NH-8 around 4 pm when both the boys were returning from their work from National Brain Research Centre (NBRC) in Manesar."  -> nh-8, manesar ( NSG camp is not detected )


Time :
1. sentences which have time info are not selected by sent_selector

Location Accuracy = 77.84 %
Time Accuracy = 63.29 %

# Pending Pipeline
1. get pinpointed location and time from clauses between prepositions
2. get number of casualities by analysing the subject part of sentences and developing a similar procedure for casualities
3. integrate the processes of getting loc, time and casualities
4. getting coordinates from location names - done
5. data plotting - done

# Notes to self
1. sent_selector7.py and sent_selector7_beta.py are same except that beta version also prints certain things


# Pending Issues:
1. body output - may 2017 - day11, article 0 - body has numbers 1 to 6 in it.
	=== solve after rerunning pipeline on may 2017
	
2. sentence tokenizer made this split:
In another spine-chilling accident, a 20-year-old engineering student died after ramming his i20 into a road divider at high speed near Green Mosque on Road No.
3, Banjara Hills on Tuesday afternoon.

	=== soln - replace No. with number, Mr. with mister == done

3. we need to use the sentence selector to eliminate the negative examples of accidents news from the selected sentences. The negative examples tend to have few/no instances of verb which are important to us.

	=== remove sentence having score=0 or (score = some threshold) == done

4. limit the number of sentences that are marked relevant on basis of "took place" to 1.
	=== implement this == done


# Meeting - Prof. Bedathur
1. Try heidel-time (really good), gu-time tagger11
2. run pos tagger on whole sentence(to give context) and then select location based on tag of words obtained by splitting on prepositions
3. complete the whole pipeline once, seperately create a manually labelled set -> compare what fraction of features is our pipeline able to extract, to be able to quote a figure)
4. make your own classifiers to improve pipeline

# Negative Examples(May 2017):
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


3. for automation of pipeline -> automate openie by Popen

4. for sentence selection from openie output -> Exp with - diff weights of lists
														- adding list 0 containing only kill, die, injure
														- shuffling verbs amongst lists

5. decide if selection of sentence having "met with" is useful in sentence selection


scrapy runspider news.py -o article.json
scrapy runspider news.py -o article.jl

# Difficult to predict positive example:
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


# Baadal VM access:

ssh baadalvm@10.17.51.49
password : acam123



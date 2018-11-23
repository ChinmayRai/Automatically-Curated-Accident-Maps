Ma'am
First of all I have a question. Is demo like a presentation of say 20-30 min or is it like a stall that we need to setup as in case of an exhibition?

I think the demo should contain the following:
1. A short usage of the tool in which we dont explain the tool. Simply show that this is the input and this is the output
2. We should make modules of the code as follows:
	1. Web Crawler + OpenIE preprocessor - input = link of archive, crawls data , classifies +ve examples, preprocessing for openie
	(in order to run the system live there, we will need internet access. I have requested ICTD authorities for the same)

	The individual parts are already made. we need to combine them to make them 1.

	2. running OpenIE
	(takes time)

	Right now, we transfer the crawled data on baadal vm, then run OpenIE and then bring back the output of openIE to our system.
	We have to make a script that does all of this itself.

	3. different extractors for diff types of information + geotagging + plotting:
		1. Location and time
		2. Number of Casualty
		3. Cause Detection (Optional)

	The extractors and location, time, number of casualties are made. Their accuracy has to be improved. Extractor for cause detection has to be made.
	Presently, the accuracies are:
			Location Accuracy = 77.84%		Time Accuracy = 63.29 %
	Additionally, the accuracy of the geotagger needs a lot of improvement.

	Regarding improvement of accuracy of geotagger, we dont have any starting point on how to proceed.

	We were also thinking on building some GUI to show the openIE output.

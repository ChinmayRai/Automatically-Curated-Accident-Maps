1. Casualty -
	a.	works for:

		Singular pronoun : he/she
		Singular proper noun
		A noun
		The duo

		== hardcoding certain key words eg. couple, duo

	== if there are multiple numbers separated by 'and', split them heuristically at and, recursively find number and add
	~ignoring this for now as there are very few instances of and~

		Person and n others
		Person and his/her relative(s)
		Person and n of his colleagues/relatives
		No one

	== add seperate rule for including
		N people, including m children/women
		~ very few instances so not implemented~

	== ignore coreference resolution for now
		They

	inanimate objects - (the car, the truck ) have to be excluded
	== use wordnet to identify inanimate or not
		http://wordnetweb.princeton.edu/perl/webwn
	== if number is followed by a Person noun (you can check it in Wordnet) and has right plurality
	~not implemented~

	== if number is associated with year then discard it
		add specific rules ( ____ year old ;
							 <name>, ____, was killed ... )
		Person name, age
		A n-year old man/woman

	Exceptions:
	1. ten people, including two children
	[(10, 0), (2, 3)]

	2. at least 15,642 people
	[]

2. Cause
	== leave for now, do the report. Do it before presentation(Jan).
		about 15 classes(causes of accidents). Annotate ~30~ examples for each class. train(try with logistic regression).

3. testing
		golden set = 100 articles

		Accuracy in Location Detection = 77.8% 
		Accuracy in Time Detection = 63.29% 

		a. time clause  - trigger verbs not effective
			== show examples of failures to sir

		b. automate?
			== see fraction of words matched with expectation


4. Plotting
	== debug why some points are plotted in US




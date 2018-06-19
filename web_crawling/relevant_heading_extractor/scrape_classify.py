import json
import sys
import headlines
from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
from fractions import Fraction
from sklearn import metrics
import numpy as np
import pickle
from sklearn import svm
import timeit

start = timeit.default_timer()

text_clf = pickle.load(open('finalized_model.sav', 'rb'))
f=open("final.json", "w+")
f.write("[")
u=0
for date in range(1,31):
	t1 = timeit.default_timer()
	index=date+42886
	link="/2017/6/"+str(date)+"/archivelist/year-2017,month-6,starttime-"+str(index)+".cms"

	j=headlines.extract(link)
	l=j['title'];
	a=text_clf.predict(l);
	z=0
	if(u==0):
		f.write("[")
		u=1
	elif(u==1):
		f.write(",[")
	for i in range(0,len(a)):
		if(a[i]==1):
			if(z==0):
				f.write("\"")
				z=1
			elif(z==1):
				f.write(",\"")		
			f.write(j["url"][i])
			f.write("\"\n")
	f.write("]")
	print(str(date)+"\n")
	t2 = timeit.default_timer()
	print(t2-t1)


f.write("]")
f.close()

stop = timeit.default_timer()
print ("total="+str(stop-start))

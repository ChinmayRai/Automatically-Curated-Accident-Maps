import json
import sys
from sklearn.feature_extraction.text import CountVectorizer
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
from fractions import Fraction
from sklearn import metrics
import numpy as np
import pickle
from sklearn import svm

text_clf = pickle.load(open('finalized_model.sav', 'rb'))



def check(str):
	n=text_clf.predict([str])[0]
	return n

print(check(sys.argv[1]))
"""


file_object = open(r"test.json","r")
title = file_object.read()
p = json.loads(title)
file_object.close()

t=[]
for i in p:
	t.append(i)

b=text_clf.predict(t);

h=[0]*(len(t))
for x in range(888,1001):
	h[x]=1;

print("accuracy="+str(np.mean(b == h)))  
tp=0
fp=0
tn=0
fn=0

for i in range(0,1000):
	if(b[i]==1 and h[i]==1):
		tp += 1
	elif(b[i]==1 and h[i]==0):
		fp += 1
	elif(b[i]==0 and h[i]==0):
		tn += 1
	else:
		fn += 1

pre=Fraction(tp,(tp+fp))

rec=Fraction(tp,(tp+fn))
f1=Fraction((pre*rec),(pre+rec))

print("precision="+str(float(pre)))
print("recall="+str(float(rec)))
print("f1 score="+str(float(f1)))
"""
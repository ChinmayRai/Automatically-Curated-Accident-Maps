import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.model_selection import GridSearchCV
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
from sklearn.datasets import fetch_20newsgroups
from fractions import Fraction
from sklearn import metrics
import numpy as np
from sklearn import svm
import pickle

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]


# Reading the Training Set in
file_object1 = open(r"training.json","r")
titles = file_object1.read()
k = json.loads(titles)
file_object1.close()

l=[]
for i in k:
	l.append(i)


stop= frozenset(["a", "the","all","up","at","to","by","of","for","as","from","our","held","\u","written","update","govt","Jan","January","Feb","March","April","May","June","July","aug","August","sept","oct","october","Nov","November","Dec","December",
					"get","against","city","lakh","arrested","day","court","family","kapoor","government","khan","crore","BJP","PM","congress","modi","cbse","singh","first","here","delhi","mumbai","world","fire","schools"])
#stop_words=stop,tokenizer=LemmaTokenizer()

# create the transform
vectorizer = CountVectorizer(ngram_range=(1, 2),token_pattern=r'\b\w+\b',stop_words=stop,tokenizer=LemmaTokenizer())
#vectorizer=HashingVectorizer(n_features=2**12)
# tokenize and build vocab
vectorizer.fit(l)
# summarize
#print(vectorizer.vocabulary)
# encode document
vector = vectorizer.transform(l)
# summarize encoded vector
f=vector.shape
print(f)
#convert the vector to array
a=[[]*(f[1]) for x in xrange(f[0])]
a=vector.toarray()

#creating the array of labels
b=[0]*(f[0])
for x in range(1583,1937):
	b[x]=1;


clf = svm.SVC(C=58.25,gamma=0.0009)

clf.fit(a,b)  

"""
x=["Accident-prone Bypass back on Lalbazar radar"]

print(clf.predict((vectorizer.transform(x)).toarray()))

"""
#test set

file_object = open(r"test.json","r")
title = file_object.read()
p = json.loads(title)
file_object.close()

t=[]
for i in p:
	t.append(i)

print(len(t))
vec = vectorizer.transform(t)
c=vec.toarray()

b=clf.predict(c);


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

#print(metrics.classification_report(h, b,target_names=['accident news','non_accident news']))

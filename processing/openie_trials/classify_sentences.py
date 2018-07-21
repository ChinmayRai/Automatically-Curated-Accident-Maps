import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from nltk import word_tokenize          
from nltk.stem import WordNetLemmatizer 
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
file_object1 = open(r"irrelevant.json","r")
t = file_object1.read()
k = json.loads(t)
file_object1.close()

l=[]
for i in k:
	l.append(i)

print(len(l));
n=len(l);

file_object = open(r"Relevant.json","r")
t1 = file_object.read()
k1 = json.loads(t1)
file_object.close()

for i in k1:
	l.append(i)

print(len(l));

#creating the array of labels
b=[0]*(len(l))
for x in range(n,len(l)):
	b[x]=1;


text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,3),token_pattern=r'\b\w+\b')),('tfidf', TfidfTransformer()),('clf', svm.SVC(gamma=0.001, C=100.))])
  

data=[l,b]

X_train, X_test= train_test_split(l,test_size=0.25)
y_train, y_test= train_test_split(b,test_size=0.25)
#gs_clf = GridSearchCV(text_clf, parameters,verbose=2)
#gs_clf.fit(l,b)

text_clf.fit(X_train,y_train)
y_pred = text_clf.predict(X_test)

print(np.mean(y_pred==y_test))

target_names = ['-', '+']
print(metrics.classification_report(y_test, y_pred,target_names=target_names))
"""
#classification
file_object = open(r"june_2017_sent_token.json","r")
month = file_object.read()
month = json.loads(month)
file_object.close()

for date in month:
	for article in date:
		para = article['body']
		for sentence in para:
			x=[sentence]
			if (text_clf.predict(x)==0):
				para.remove(sentence)


with open('june_relevant_Tfidf.json', 'w+') as outfile:
    json.dump(month, outfile)
"""
#print(text_clf.predict(x))
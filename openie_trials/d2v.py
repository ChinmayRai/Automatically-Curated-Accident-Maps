from gensim.utils import simple_preprocess
from gensim.models.doc2vec import Doc2Vec,TaggedDocument
from random import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn import metrics
import os
import collections
import smart_open
import random
import json

def vec_for_learning(doc2vec_model, sents):
    targets, regressors = zip(*[(doc.tags[0], doc2vec_model.infer_vector(doc.words, steps=20)) for doc in sents])
    return targets, regressors

file_object1 = open(r"irrelevant.json","r")
t = file_object1.read()
k = json.loads(t)
file_object1.close()

l=[]
for i in k:
	l.append(i)

n=len(l);

file_object = open(r"Relevant.json","r")
t1 = file_object.read()
k1 = json.loads(t1)
file_object.close()

for i in k1:
	l.append(i)

sents=[]

for i in range(0,n):
	sents.append(TaggedDocument(simple_preprocess(l[i]),tags=[0]))

for i in range(n,len(l)):
	sents.append(TaggedDocument(simple_preprocess(l[i]),tags=[1]))



train_data, test_data = train_test_split(sents,test_size=0.25)
model = Doc2Vec(train_data, vector_size=50, window=100, epochs=20, dm=1)

y_train, X_train = vec_for_learning(model, train_data)
y_test, X_test = vec_for_learning(model, test_data)



logreg = LogisticRegression(C=0.5,class_weight='balanced')#, "clf__estimator__class_weight": ['balanced', None],
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

print(np.mean(y_pred==y_test))

target_names = ['-', '+']
print(metrics.classification_report(y_test, y_pred,target_names=target_names))






"""

model = Doc2Vec(sents, vector_size=50, window=100, epochs=20, dm=1)
y, X = vec_for_learning(model, sents)
logreg = LogisticRegression()
logreg.fit(X, y)

file_object = open(r"june_2017_sent_token.json","r")
month = file_object.read()
month = json.loads(month)
file_object.close()

for date in month:
	for article in date:
		para = article['body']
		for sentence in para:
			x=[model.infer_vector(sentence, steps=20)]
			if (logreg.predict(x)==0):
				para.remove(sentence)


with open('june_relevant_d2v_logreg.json', 'w+') as outfile:
    json.dump(month, outfile)

"""
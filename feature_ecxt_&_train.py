import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

file_object = open(r"headings.json","r")
headings = file_object.read()
j = json.loads(headings)

file_object.close()

l=[]
for i in j[0]['title']:
	l.append(i)

file_object = open(r"positive_examples_titles.json","r")
titles = file_object.read()
k = json.loads(titles)
file_object.close()

for i in k:
	l.append(i['title'])


# list of text documents
#text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(l)
# summarize
#print(vectorizer.vocabulary_)
# encode document
vector = vectorizer.transform(l)

# summarize encoded vector
f=vector.shape
print(f)
a=[[]*(f[1]) for x in xrange(f[0])]
a=vector.toarray()
print(a)



b=[0]*(803)

b[157]=1
b[178]=1;
b[676]=1;

for x in range(700,802):
	b[x]=1;


clf = svm.SVC(gamma=0.001, C=100.)

clf.fit(a,b) 


#test set

file_object = open(r"26may.json","r")
title = file_object.read()
p = json.loads(title)
file_object.close()

t=[]

for i in j[0]['title']:
	t.append(i)

print(len(t))

vec = vectorizer.transform(t)
c=vec.toarray()


for i in range(0,len(t)-1):
	print(clf.predict([c[i]]))




import json
from sklearn.feature_extraction.text import CountVectorizer

file_object = open(r"positive_examples_may18.json","r")
titles = file_object.read()
j = json.loads(titles)
file_object.close()

l=[]
for i in j:
	l.append(i['title'])

# uncomment to print the list
# for i in l:
# 	print i

vectorizer = CountVectorizer()
vectorizer.fit(l)
print(vectorizer.vocabulary_)

vector = vectorizer.transform(l)
print("shape of vector = "),
shape = vector.shape
print shape

m = vector.toarray()
# for i in range(5):
# 	print m[i]

freq = [0]*shape[1]
for i in m:
	freq = freq + i

# print freq

# f = [0]*shape[1]
# for i in m:
# 	f = [f[x]+i[x] for x in range(len(f))]

a=[4,1,2,3,5]
a.sort(reverse=True)
print a

freq = freq.tolist()
print type(a)
print type(freq)

freq.sort(reverse=True)
print freq
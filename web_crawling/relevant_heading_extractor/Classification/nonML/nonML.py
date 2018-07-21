import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

file_object = open(r"positive_examples_may18.json","r")
titles = file_object.read()
j = json.loads(titles)
file_object.close()

l=[]
for i in j:
	l.append((i['title'],1))

#number of positive examples
pos = len(l)

file_object = open(r"negative_examples.json","r")
titles = file_object.read()
j = json.loads(titles)
file_object.close()

for i in j[0]['title']:
	l.append((i,0))

#number of negative examples
neg = len(l) - pos

# uncomment to print the list
# for i in l:
# 	print i

l2=[]
for i in l:
	l2.append(i[0])

# print l2

vectorizer = CountVectorizer()
vectorizer.fit(l2)
# print(vectorizer.vocabulary_)

vector = vectorizer.transform(l2)
print("shape of vector = "),
shape = vector.shape
print shape

m = vector.toarray()
# for i in range(5):
# 	print m[i]




freq_pos = np.asarray([0]*shape[1],dtype = float)

for i in range(pos):
	freq_pos = freq_pos + m[i]

freq_pos_norm = freq_pos * (10.0/pos)

freq_neg = np.asarray([0]*shape[1],dtype = float)
for i in range(neg):
	freq_neg = freq_neg + m[pos + i]

# print type(freq_neg)
freq_neg_norm = freq_neg  * (10.0/neg)

features = freq_pos_norm - freq_neg_norm

for i in range(shape[1]):
	# print freq_pos[i],
	# print " ",
	# print freq_neg[i],
	# print " ",
	# print freq_pos_norm[i],
	# print " ",
	# print freq_neg_norm[i],
	# print " ",
	print features[i]

# for i in features:
# 	print '{0:.10f}'.format(i)

# def dis(x):
# 	for i in x:
# 		print '{0:.10f}'.format(i)







# f = [0]*shape[1]
# for i in m:
# 	f = [f[x]+i[x] for x in range(len(f))]

# a=[4,1,2,3,5]
# a.sort(reverse=True)
# print a

# freq = freq.tolist()
# print type(a)
# print type(freq)

# freq.sort(reverse=True)
# print freq
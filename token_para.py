import collections
print(collections) 

import nltk
from nltk.tokenize import sent_tokenize

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(nltk.sent_tokenize(data))
# DESCRIPTION = detect cause of accident, outputs appropriate labels

import json
# import sys
# from nltk.stem.wordnet import WordNetLemmatizer
# from num_casualty import num_casualty

# return true if sub is found in the body or title of the article
def find(sub):
	return (article["body"].lower().find(sub)!=-1 or article["title"].lower().find(sub)!=-1)


infile="article_body.json"
outfile="cause.json"


file_object = open(infile,"r")
article = file_object.read()
article = json.loads(article)

# drunk
# rash driving
# 'tyre' and 'burst' or 'flat tyre'
# negligence
# Speeding / overspeed
# lost control
# mowed / run over / ran over / knocked down
# falling asleep / sleep-deprived / fallen asleep / dozed off
# accident-prone
# topple/overturned

labels=[]
if(find("drunk")):
	labels.append("drunk_driving")

if(find("rash driving")):
	labels.append("rash_driving")

if( (find("tyre") and find("burst")) or find("flat tyre") ):
	labels.append("tyre_related")

if(find("negligence")):
	labels.append("negligence")

if( find("speeding") or find("overspeed") ):
	labels.append("overspeeding")

if(find("lost control")):
	labels.append("lost_control")

if( find("mowed") or find("run over") or find("ran over") or find("knocked down")):
	labels.append("run_over")

if( find("falling asleep") or find("sleep-deprived") or find("fallen asleep") or find("dozed off")):
	labels.append("sleep")

if( find("topple") or find("overturned") ):
	labels.append("toppling")

if(find("accident-prone")):
	labels.append("accident-prone")


# FOR JSON OUTPUT
with open(outfile, 'w+') as outfile:
    json.dump(labels, outfile)


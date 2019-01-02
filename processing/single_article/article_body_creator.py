# DESCRIPTION : takes details of article from the user via console inputs and stores them in a file as per required format

import json
import readchar

jsonOutfile="article_body.json"

title=raw_input("Enter the title of the article :\n")
repLoc=raw_input("Enter the reporting location of the article :\n")
body=raw_input("Enter the body of the article :\n")
# print("Enter the body of the article :")
# body=""
# c = readchar.readchar()
# while(c!='\n'):
# 	body+=c
# 	c=readchar.readchar()

d=dict()
d["body"]=body
d["title"]=title
d["repLoc"]=repLoc

# JSON OUTPUT
with open(jsonOutfile, 'w+') as outfile:
    json.dump(d, outfile)
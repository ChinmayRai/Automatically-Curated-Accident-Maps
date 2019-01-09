# DESCRIPTION : takes details of article from the user via console inputs and stores them in a file as per required format

import json
# import readchar

jsonOutfile="article_body.json"

title=raw_input("Enter the title of the article :\n")
repLoc=raw_input("Enter the reporting location of the article :\n")
year=raw_input("Enter the year of reporting (eg. 2019) :\n")
month=raw_input("Enter the month of reporting (eg. 1 for January) :\n")
date=raw_input("Enter the date of reporting (eg. 6 for today) :\n")
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
d["date"]=date
d["month"]=month
d["year"]=year

# JSON OUTPUT
with open(jsonOutfile, 'w+') as outfile:
    json.dump(d, outfile)
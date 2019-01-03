# python article_body_creator.py 

echo "1) Reading the following input from article_body.json : \n"
cat article_body.json
echo "\n\n================================================================================================================================================================================\n"

echo "2) Converting the body of the article to sentences\n"
python body_to_sent.py
cat article_sent_token.json
echo "\n\n================================================================================================================================================================================\n"

echo "3) Formatting sentences according to the input format of OpenIE\n"
python sent_to_openie.py
cat article_openie_input.txt
echo "\n\n================================================================================================================================================================================\n"

echo "4) Processing the sentences with OpenIE\n"
cd ~/Documents/softwares/OpenIE-standalone/
java -Xmx10g -XX:+UseConcMarkSweepGC -jar openie-assembly.jar --split ~/Documents/SURA/processing/single_article/article_openie_input.txt ~/Documents/SURA/processing/single_article/article_openie_output.txt
cd ~/Documents/SURA/processing/single_article/
cat article_openie_output.txt
echo "\n\n================================================================================================================================================================================\n"

echo "5) Extracting number of casualties\n"
python sent_selector7_casualty.py
echo "Number of Casualties = "
cat num_casualty.json
echo "\n\n================================================================================================================================================================================\n"

echo "6) Extracting Time of Accident\n"
python sent_selector7.py
python merge_prep_clause.py
python3 temporal.py
echo "\n"
cat time.json
echo "\n\n================================================================================================================================================================================\n"

echo "7) Extracting Location of Accident\n"
python get_proper_noun.py
cat prop_noun_clauses.json
echo "\n\n================================================================================================================================================================================\n"

echo "8) Formatting the output features for mapping\n"
python formater.py
cat formatted_for_mapbox.json
echo "\n\n================================================================================================================================================================================\n"

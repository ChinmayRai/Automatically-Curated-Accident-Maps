# python article_body_creator.py 
python body_to_sent.py
echo "converted body to sentences"
python sent_to_openie.py
echo "formatted sentences acc to openie"

# mv article_openie_input.txt ~/Documents/softwares/OpenIE-standalone/.
cd ~/Documents/softwares/OpenIE-standalone/
java -Xmx10g -XX:+UseConcMarkSweepGC -jar openie-assembly.jar --split ~/Documents/SURA/processing/single_article/article_openie_input.txt ~/Documents/SURA/processing/single_article/article_openie_output.txt
cd ~/Documents/SURA/processing/single_article/
echo "processed in openie"

python sent_selector7_casualty.py
echo "casualty done"

python sent_selector7.py
python merge_prep_clause.py
python3 temporal.py
echo "time done, reduced the set of clauses"

python get_proper_noun.py
echo "location done"

python formater.py
echo "formating done, check file formatted_for_mapbox.json"

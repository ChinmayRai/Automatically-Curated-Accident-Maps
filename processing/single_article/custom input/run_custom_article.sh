# python article_body_creator.py 
python body_to_sent.py
echo "converted body to sentences"
python sent_to_openie.py
echo "formatted sentences acc to openie"

# mv article_openie_input.txt ~/Documents/softwares/OpenIE-standalone/.
cd ~/Documents/softwares/OpenIE-standalone/
java -Xmx10g -XX:+UseConcMarkSweepGC -jar openie-assembly.jar --split ~/Documents/SURA/processing/single_article/custom\ input/article_openie_input.txt ~/Documents/SURA/processing/single_article/custom\ input/article_openie_output.txt
cd ~/Documents/SURA/processing/single_article/custom\ input/
echo "processed in openie"


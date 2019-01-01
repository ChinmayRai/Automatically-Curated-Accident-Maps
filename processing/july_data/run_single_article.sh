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

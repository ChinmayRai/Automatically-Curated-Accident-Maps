python sent_selector7_casualty.py
echo "casualty done"

python sent_selector7.py
python merge_prep_clause.py
# $1=date, $2=month, $3=year
python3 temporal.py $1 $2 $3
echo "time done, reduced the set of clauses"

python get_proper_noun.py
echo "location done"

python formater.py
echo "formating done, check file formatted_for_mapbox.json"

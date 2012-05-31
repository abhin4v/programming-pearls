echo `date +%T` "Generating input"
python problem4.py $1 $2 > input
echo `date +%T` "Generating output"
cat input | python problem3.py $1 > output
echo `date +%T` "Sorting input"
sort -g input > input_sorted
echo `date +%T` "Diffing sorted input and output"
diff -s input_sorted output
rm input input_sorted output
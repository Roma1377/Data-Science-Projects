#!/bin/sh
files=$(ls [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].csv 2>/dev/null | sort)
if [ -z "$files" ]; then
    echo "No CSV files found."
    exit 1
fi
first_file=$(echo "$files" | head -n1)
head -n1 "$first_file" > hh_positions.csv
for file in $files; do
    tail -n +2 "$file" >> hh_positions.csv
done
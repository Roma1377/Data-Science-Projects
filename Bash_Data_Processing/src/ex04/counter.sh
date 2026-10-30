#!/bin/sh
echo '"name","count"' > hh_uniq_positions.csv
cut -d',' -f3 ../ex03/hh_positions.csv | tail -n +2 | tr -d '"' | sort | uniq -c | sort -nr | awk '{print "\""$2"\","$1}' >> hh_uniq_positions.csv
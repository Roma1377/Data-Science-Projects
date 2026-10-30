#!/bin/sh
input="../ex03/hh_positions.csv"
gawk -v FPAT='"[^"]*"|[^,]*' '
NR == 1 {header = $0; next}
{
    datetime = $2
    gsub(/^"|"$/, "", datetime)
    date = substr(datetime, 1, 10)
    filename = date ".csv"
    if (!(date in seen)) {
        seen[date] = 1
        print header > filename
    }
    print >> filename
}
' "$input"
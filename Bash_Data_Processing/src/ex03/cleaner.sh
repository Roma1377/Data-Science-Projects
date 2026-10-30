#!/bin/sh
gawk -v FPAT='"[^"]*"|[^,]*' -v OFS=',' '
NR == 1 {print; next}
{
    name = $3
    gsub(/^"|"$/, "", name)
    n = split(name, words, /[^a-zA-Z]+/)
    levels = ""
    for (i = 1; i <= n; i++) {
        w = words[i]
        if (w == "") continue
        if (tolower(w) == "junior" || tolower(w) == "middle" || tolower(w) == "senior") {
            if (levels == "") levels = w
            else levels = levels "/" w
        }
    }
    if (levels == "") levels = "-"
    $3 = "\"" levels "\""
    print
}' ../ex02/hh_sorted.csv > hh_positions.csv
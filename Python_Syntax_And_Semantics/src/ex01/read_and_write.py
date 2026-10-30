def convert_csv_to_tsv():
    input_file = "ds.csv"
    output_file = "ds.tsv"

    with open(input_file, "r", encoding="utf-8") as inf:
        with open(output_file, "w", encoding="utf-8") as outf:
            for line in inf:
                fields = []
                current = []
                in_quotes = False
                for ch in line.rstrip("\n"):
                    if ch == '"':
                        in_quotes = not in_quotes
                    elif ch == "," and not in_quotes:
                        fields.append("".join(current))
                        current = []
                    else:
                        current.append(ch)
                fields.append("".join(current))
                outf.write("\t".join(fields) + "\n")


if __name__ == "__main__":
    convert_csv_to_tsv()

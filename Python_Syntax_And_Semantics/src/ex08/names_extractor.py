import sys


def main():
    if len(sys.argv) != 2:
        return

    input_file = sys.argv[1]
    output_file = "employees.tsv"

    with open(input_file, "r", encoding="utf-8") as inf:
        emails = [line.strip() for line in inf if line.strip()]

    with open(output_file, "w", encoding="utf-8") as outf:
        for email in emails:
            local_part = email.split("@")[0]
            name, surname = local_part.split(".")
            name = name.capitalize()
            surname = surname.capitalize()
            outf.write(f"{name}\t{surname}\t{email}\n")


if __name__ == "__main__":
    main()

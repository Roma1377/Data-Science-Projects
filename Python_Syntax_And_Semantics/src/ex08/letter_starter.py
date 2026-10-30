import sys


def main():
    if len(sys.argv) != 2:
        return

    email_target = sys.argv[1]
    employees_file = "employees.tsv"

    name = None
    with open(employees_file, "r", encoding="utf-8") as f:
        for line in f:
            fields = line.strip().split("\t")
            if len(fields) == 3 and fields[2] == email_target:
                name = fields[0]
                break

    if name:
        print(
            f" {name}, добро пожаловать в нашу команду! Мы уверены, что работать вместе с тобой будет очень приятно. Для нас это важно - мы стремимся, чтобы в компании работались именно такие люди."
        )
    else:
        print("Email not found in employees.tsv")


if __name__ == "__main__":
    main()

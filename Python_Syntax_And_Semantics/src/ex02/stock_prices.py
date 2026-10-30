import sys


def main():
    if len(sys.argv) != 2:
        return

    company_input = sys.argv[1].strip()
    COMPANIES = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "Tesla": "TSLA",
        "Nokia": "NOK",
    }
    STOCKS = {
        "AAPL": 287.73,
        "MSFT": 173.79,
        "NFLX": 416.90,
        "TSLA": 724.88,
        "NOK": 3.37,
    }

    found = False
    for name, ticker in COMPANIES.items():
        if name.lower() == company_input.lower():
            print(STOCKS[ticker])
            found = True
            break
    if not found:
        print("Unknown company")


if __name__ == "__main__":
    main()

import sys


def main():
    if len(sys.argv) != 2:
        return

    ticker_input = sys.argv[1].strip()
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

    reverse_map = {ticker: name for name, ticker in COMPANIES.items()}

    ticker_upper = ticker_input.upper()
    if ticker_upper in reverse_map:
        company = reverse_map[ticker_upper]
        price = STOCKS[ticker_upper]
        print(f"{company} {price}")
    else:
        print("Unknown ticker")


if __name__ == "__main__":
    main()

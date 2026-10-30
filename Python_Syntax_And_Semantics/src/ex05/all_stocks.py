import sys


def main():
    if len(sys.argv) != 2:
        return

    raw = sys.argv[1]
    parts = [p.strip() for p in raw.split(",")]
    if any(p == "" for p in parts):
        return

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

    companies_lower = {
        name.lower(): (name, ticker) for name, ticker in COMPANIES.items()
    }
    tickers_lower = {
        ticker.lower(): (ticker, name) for name, ticker in COMPANIES.items()
    }

    for expr in parts:
        expr_lower = expr.lower()
        if expr_lower in companies_lower:
            name, ticker = companies_lower[expr_lower]
            print(f"{name} stock price is {STOCKS[ticker]}")
        elif expr_lower in tickers_lower:
            ticker, name = tickers_lower[expr_lower]
            print(f"{ticker.upper()} is a ticker symbol for {name}")
        else:
            print(f"{expr} is an unknown company or an unknown ticker symbol")


if __name__ == "__main__":
    main()

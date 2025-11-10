import yfinance as yf
import plotly.express as px


def main():
    ticker = input("Ticker: ")
    company = yf.Ticker(ticker)
    period = input("What period would you like to see?\nOptions: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max\nPeriod: ")

    while period not in ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]:
        period = input("The period you entered is not valid.\nPeriod must be one of the following: 1d,5d,1mo,3mo,6mo,"
                       "1y,2y,5y,10y,ytd,max"
                       "\nEnter period: ")

    df = yf.Ticker(f"{ticker}").history(period=period, interval="1d").round({'Close': 2})

    fig = px.line(
        df,
        x=df.index,
        y="Close",
        title=f"{company.info['longName']}",
        labels={"Close": "Price (USD)", "index": "Date"},
        color_discrete_sequence=['purple']
    )
    fig.show()


if __name__ == '__main__':
    main()

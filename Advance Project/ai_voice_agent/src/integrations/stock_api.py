import yfinance as yf

def get_stock_price(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")["Close"].iloc[-1]
    return f"The current price of {ticker} is ${price:.2f}."

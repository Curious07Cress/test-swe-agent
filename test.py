import yfinance as yf

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    price = stock.history().tail(1)['Close'].iloc[0]
    return price

if __name__ == "__main__":
    symbol = "DASTY"
    stock_price = get_stock_price(symbol)
    print(f"The stock price of {symbol} is ${stock_price:.2f}")
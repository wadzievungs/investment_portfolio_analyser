import pandas as pd
import yfinance as yf

def load_portfolio(filepath):
    """
    Load portfolio data from the CSV file.

    Parameters:
    filepath (str): Path to the portfolio CSV file

    Returns:
    DataFrame: A pandas DataFrame containing the portfolio data 
    """
    df = pd.read_csv(filepath)
    return df

def fetch_current_prices(df):
    """
    Fetch current prices for all stocks in the portfolio.

    Parameters:
    df (DataFrame): Portfolio DataFrame with ticker, shares and purchase_price

    Returns:
    list: A list of dictionaries containing full stock information
    """
    portfolio = []

    for _, row in df.iterrows():
        ticker = row['ticker']
        shares = row['shares']
        purchase_price = row['purchase_price']

        stock = yf.Ticker(ticker)
        info = stock.info

        current_price = (info.get('current_price') or
                         info.get('regularMarketPrice', 0))
        company_name = info.get('longName', ticker)

        portfolio.append({
            'ticker': ticker,
            'company_name': company_name,
            'shares': shares,
            'purchase_price': purchase_price,
            'current_price': current_price
        }) 

        print(f"Fetched data for {company_name}...")

    return portfolio
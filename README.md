# Invetment Portfolio Analyser

A python tool that fetches live stock market data for multiple stocks and analyses the performance of an entire investment portfolio.
Built as Project 4 of my FinTech portfolio.

## What it does 
- Reads a portfolio of stocks from a CSV file
- Fetches live market prices for each stock from Yahoo Finance
- Calculates cost basis, market value, gain/loss and return percentage
- Displays a complete breakdown for each stock
- Shows overall portfolio summary with total gains and return
- Identifies the best and worst performing stocks

## Technologies used
- Python 3
- yfinance
- pandas

## How to run it
1. Clone this repository
2. Install dependencies: pip install yfinance pandas
3. Edit data/portfolio.csv with your own stocks
4. Navigate to the src folder
5. Run: python main.py

## Portfolio CSV format
ticker,shares,purchase_price
AAPL,10,150.00
MSFT,5,280.00
GOOGL,3,140.00

## Example output
==================================================
         INVESTMENT PORTFOLIO ANALYSER
==================================================

Fetching live market data, please wait...
Fetched data for Apple Inc....
Fetched data for Microsoft Corporation...
Fetched data for Alphabet Inc....
Fetched data for Tesla, Inc....
Fetched data for Naspers Limited...

==================================================
          STOCK PERFORMANCE
==================================================

Apple Inc. (AAPL)
  Shares:          10
  Purchase Price:  $150.00
  Current Price:   $294.30
  Cost Basis:      $1,500.00
  Market Value:    $2,943.00
  Gain/Loss:       +$1,443.00
  Return:          +96.20%
==================================================

Microsoft Corporation (MSFT)
  Shares:          5
  Purchase Price:  $280.00
  Current Price:   $373.94
  Cost Basis:      $1,400.00
  Market Value:    $1,869.70
  Gain/Loss:       +$469.70
  Return:          +33.55%
==================================================

Alphabet Inc. (GOOGL)
  Shares:          3
  Purchase Price:  $140.00
  Current Price:   $346.13
  Cost Basis:      $420.00
  Market Value:    $1,038.39
  Gain/Loss:       +$618.39
  Return:          +147.24%
==================================================

Tesla, Inc. (TSLA)
  Shares:          8
  Purchase Price:  $200.00
  Current Price:   $381.61
  Cost Basis:      $1,600.00
  Market Value:    $3,052.88
  Gain/Loss:       +$1,452.88
  Return:          +90.81%
==================================================

Naspers Limited (NPN.JO)
  Shares:          15
  Purchase Price:  $3,200.00
  Current Price:   $81,368.00
  Cost Basis:      $48,000.00
  Market Value:    $1,220,520.00
  Gain/Loss:       +$1,172,520.00
  Return:          +2,442.75%
==================================================

==================================================
         PORTFOLIO SUMMARY
==================================================
Total Invested:     $52,920.00
Total Value:        $1,229,423.97
Total Gain/Loss:    +$1,176,503.97
Overall Return:     +2,223.17%
==================================================

==================================================
         BEST & WORST PERFORMERS
==================================================
Best Performer:  Naspers Limited (NPN.JO)
                 +2,442.75%
Worst Performer: Microsoft Corporation (MSFT)
                 +33.55%
==================================================

## Key concepts used
- Data pipeline architecture
- Live API data fetching
- Financial calculations (cost basis, market value, return %)
- Lambda functions for sorting
- Generator expressions for summing data

## What I learned
- How to build a data pipeline in Python
- How to analyse multiple stocks simultaneously
- How to calculate investment returns professionally
- How to work with stocks across different exchanges
- How currency differences affect international portfolios

## Author
Wadzanai Vunganai
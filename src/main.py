import os 
from portfolio import load_portfolio, fetch_current_prices
from analyser import (analyse_portfolio, get_best_performer,
                      get_worst_performer, get_portfolio_summary)

def display_header():
    """Display the program header."""
    print("=" * 50)
    print("         INVESTMENT PORTFOLIO ANALYSER")
    print("=" * 50)

def display_stock_performance(portfolio_analysis):
    """Display performance metrics for each stock."""
    print("\n" + "=" * 50)
    print("          STOCK PERFORMANCE")
    print("=" * 50)

    for stock in portfolio_analysis:
        gain_symbol = "+" if stock['gain_loss'] >= 0 else ""

        print(f"\n{stock['company_name']} ({stock['ticker']})")
        print(f"  Shares:          {stock['shares']}")
        print(f"  Purchase Price:  ${stock['purchase_price']:,.2f}")
        print(f"  Current Price:   ${stock['current_price']:,.2f}")
        print(f"  Cost Basis:      ${stock['cost_basis']:,.2f}")
        print(f"  Market Value:    ${stock['market_value']:,.2f}")
        print(f"  Gain/Loss:       {gain_symbol}${stock['gain_loss']:,.2f}")
        print(f"  Return:          {gain_symbol}{stock['return_percentage']:,.2f}%")
        print("=" * 50)

def display_portfolio_summary(summary):
    """Display overall portfolio performance."""
    gain_symbol = "+" if summary['total_gain_loss'] >= 0 else ""

    print("\n" + "=" * 50)
    print("         PORTFOLIO SUMMARY")
    print("=" * 50)
    print(f"Total Invested:     ${summary['total_cost']:,.2f}")
    print(f"Total Value:        ${summary['total_value']:,.2f}")
    print(f"Total Gain/Loss:    {gain_symbol}${summary['total_gain_loss']:,.2f}")
    print(f"Overall Return:     {gain_symbol}{summary['total_return_percentage']:,.2f}%") 
    print("=" * 50)

def display_best_worst(best, worst):
    """Display the best and worst performing stocks."""

    best_symbol = "+" if best['return_percentage'] >= 0 else ""
    worst_symbol = "+" if worst['return_percentage'] >= 0 else ""
    
    print("\n" + "=" * 50)
    print("         BEST & WORST PERFORMERS")
    print("=" * 50)
    print(f"Best Performer:  {best['company_name']} ({best['ticker']})")
    print(f"                 {best_symbol}{best['return_percentage']:,.2f}%")
    print(f"Worst Performer: {worst['company_name']} ({worst['ticker']})")
    print(f"                 {worst_symbol}{worst['return_percentage']:,.2f}%")
    print("=" * 50)

def main():
    """Main function that runs the portfolio analyser."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, 'data', 'portfolio.csv')

    display_header()
    print("\nFetching live market data, please wait...")

    df = load_portfolio(filepath)
    portfolio = fetch_current_prices(df)
    portfolio_analysis = analyse_portfolio(portfolio)
    summary = get_portfolio_summary(portfolio_analysis)
    best = get_best_performer(portfolio_analysis)
    worst = get_worst_performer(portfolio_analysis)

    display_stock_performance(portfolio_analysis)
    display_portfolio_summary(summary)
    display_best_worst(best, worst)

main()

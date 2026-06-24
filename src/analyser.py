def calculate_stock_perfomance(stock):
    """
    Calculate performance metrics for a single stock

    Parameters:
    stock (dict): Dictionary containing stock information

    Returns:
    dict: Stock information with performance metrics added
    """
    shares = stock['shares']
    purchase_price = stock['purchase_price']
    current_price = stock['current_price']

    cost_basis = shares * purchase_price
    market_value = shares * current_price
    gain_loss = market_value - cost_basis
    return_percentage = (gain_loss / cost_basis) * 100

    return {
        'ticker': stock['ticker'],
        'company_name': stock['company_name'],
        'shares': shares,
        'purchase_price': purchase_price,
        'current_price': current_price,
        'cost_basis': cost_basis,
        'market_value': market_value,
        'gain_loss': gain_loss,
        'return_percentage': return_percentage
    }

def analyse_portfolio(portfolio):
    """
    Analyse all stocks in the portfolio.

    Parameters: 
    portfolio (list): List of stock dictionaries

    Returns:
    list: List of stock dictionaries with performance metrics
    """
    portfolio_analysis = []

    for stock in portfolio:
        stock_performance = calculate_stock_perfomance(stock)
        portfolio_analysis.append(stock_performance)

    return portfolio_analysis

def get_best_performer(portfolio_analysis):
    """
    Find the best performing stock by return percentage.

    Parameters:
    portfolio_analysis (list): List of analysed stock dictionaries

    Returns:
    dict: The best performing stock dictionary
    """
    return max(portfolio_analysis, key=lambda x: x['return_percentage'])

def get_worst_performer(portfolio_analysis):
    """
    Find the worst performing stock by return percentage.

    Parameters:
    portfolio_analysis (list): List of analysed stock dictionaries

    Returns:
    dict: The worst performing stock dictionary
    """
    return min(portfolio_analysis, key=lambda x: x['return_percentage'])

def get_portfolio_summary(portfolio_analysis):
    """
    Calculate overall portfolio perfomance.

    Parameters:
    portfolio_analysis (list): List of analysed stock dictionaries

    Returns:
    dict: Overall portfolio performance metrics
    """
    total_cost = sum(stock['cost_basis'] for stock in portfolio_analysis)
    total_value = sum(stock['market_value'] for stock in portfolio_analysis)
    total_gain_loss = total_value - total_cost
    total_return_percentage = (total_gain_loss / total_cost) * 100

    return {
        'total_cost': total_cost,
        'total_value': total_value,
        'total_gain_loss': total_gain_loss,
        'total_return_percentage': total_return_percentage
    }
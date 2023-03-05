import pandas as pd
import numpy as np
import yfinance as yf

# Define the tickers of the ETFs
tickers = ["SCHA", "SCHF", "SCHH", "SCHV"]

# Define the investment amount
investment_amount = 541

# Download the historical data for the ETFs
data = yf.download(tickers, start="2010-01-01", end="2022-03-04")["Adj Close"]

# Calculate the daily returns for each ETF
returns = data.pct_change()

# Calculate the mean daily return and the covariance matrix of daily returns for each ETF
mean_daily_returns = returns.mean()
cov_matrix = returns.cov()

# Define a function to calculate the efficient frontier
def calculate_efficient_frontier(mean_returns, cov_matrix, num_portfolios=10000):
    # Generate random portfolios
    results = np.zeros((num_portfolios, len(mean_returns) +2))
    for i in range(num_portfolios):
        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)
        portfolio_return = np.dot(mean_returns, weights)
        portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        results[i,:] = [portfolio_return, portfolio_std_dev] + list(weights)
    results = pd.DataFrame(results, columns=["Return", "StdDev"]+tickers)
    
    # Find the portfolio with the highest Sharpe ratio
    risk_free_rate = 0.02
    results["SharpeRatio"] = (results["Return"] - risk_free_rate) / results["StdDev"]
    max_sharpe_idx = results["SharpeRatio"].idxmax()
    weights = results.iloc[max_sharpe_idx, 2:]
    
    # Return the efficient frontier and the weights of the portfolio with the highest Sharpe ratio
    return results, weights

# Calculate the efficient frontier
results, weights = calculate_efficient_frontier(mean_daily_returns, cov_matrix)

# Calculate the number of shares to purchase for each ETF based on the weights of the portfolio with the highest Sharpe ratio
prices = data.iloc[-1]
shares = np.round((investment_amount * weights) / prices,0)
for i in range(len(tickers)):
    print(f"Buy {shares[i]} shares of {tickers[i]}")

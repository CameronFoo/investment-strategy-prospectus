import yfinance as yf
import pandas as pd
import numpy as np
import quantstats as qs
import matplotlib.pyplot as plt

tickers_portfolio = ['JPM','BAC','TSLA','NVDA','GE','MSFT','AAPL','^FVX']
benchmark_ticker = ['^GSPC']

portfolio_data = yf.download(tickers_portfolio, start = "2014-11-01", end = "2024-10-31", interval = '1mo', progress = False)
portfolio_data = portfolio_data['Adj Close']
portfolio_data.head()

benchmark_data = yf.download(benchmark_ticker, start = "2014-11-01", end = "2024-10-31", interval = '1mo', progress = False)
benchmark_data = benchmark_data['Adj Close']

# Plots of stocks in the portfolio
portfolio_data.loc[:,['JPM','BAC','TSLA','NVDA','GE','MSFT','AAPL','^FVX']].plot(figsize=(12, 6), title='Portfolio Securities Performance')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')
plt.grid(True)
plt.show()

# Calculate log returns for all assets (including benchmark)
portfolio_data = np.log(portfolio_data) - np.log(portfolio_data.shift(1))
benchmark_data['Returns'] = np.log(benchmark_data['^GSPC']) - np.log(benchmark_data['^GSPC'].shift(1))

# Drop missing values (all rows with any NaNs)
portfolio_data = portfolio_data.dropna()
benchmark_data = benchmark_data.dropna()

# Calculate portfolio returns (weighted sum of log returns)
portfolio_data['Returns'] = (
    portfolio_data['AAPL'] * 0.1 +
    portfolio_data['BAC'] * 0.07 +
    portfolio_data['GE'] * 0.12 +
    portfolio_data['JPM'] * 0.1 +
    portfolio_data['MSFT'] * 0.12 +
    portfolio_data['NVDA'] * 0.12 +
    portfolio_data['TSLA'] * 0.07 +
    portfolio_data['^FVX'] * 0.3
)

portfolio_data.head()

# Plot of the monthly returns against the benchmark
plt.figure(figsize=(12, 6))
plt.plot(portfolio_data['Returns'], label='Portfolio Returns')
plt.plot(benchmark_data['Returns'], label='Benchmark Returns (^GSPC)')
plt.title('Portfolio vs. Benchmark Returns (Monthly)')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.legend()
plt.grid(True)
plt.show()


def annual_returns(data):
#Resample to annual frequency and calculate the mean (Use help of AI to find the annual returns)
  annual_data = data['Returns'].resample('Y').mean()

  return annual_data

# Calculate annual returns for the portfolio
portfolio_annual_returns = annual_returns(portfolio_data)
print("Portfolio Annual Returns:\n", portfolio_annual_returns)

# Calculate annual returns for the benchmark
benchmark_annual_returns = annual_returns(benchmark_data)
print("\nBenchmark Annual Returns:\n", benchmark_annual_returns)

# computing cumulative returns
portfolio_data['Cumulative Returns'] = (1+portfolio_data['Returns']).cumprod()-1
portfolio_data['Cumulative Returns'] = portfolio_data['Cumulative Returns'].dropna()

benchmark_data['Cumulative Returns'] = (1+benchmark_data['Returns']).cumprod()-1
benchmark_data['Cumulative Returns'] = benchmark_data['Cumulative Returns'].dropna()

benchmark_data.head()

# Plot the cum returns against the benchmakr SNP500
portfolio_data['Cumulative Returns'].plot(title="Portfolio Return", label='Portfolio')
benchmark_data['Cumulative Returns'].plot(title="S&P500 Return", label='S&P 500')

plt.title('Portfolio and Benchmark Cumulative Return')
plt.xlabel('Date')
plt.ylabel('Return')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.show()

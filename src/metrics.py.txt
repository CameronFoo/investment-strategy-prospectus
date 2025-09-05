tickers = ['JPMORGAN CHASE & CO. (XNYS:JPM)', 'BANK OF AMERICA CORPORATION (XNYS:BAC)', 'TESLA, INC. (XNAS:TSLA)',
           'NVIDIA CORPORATION (XNAS:NVDA)', 'GENERAL ELECTRIC COMPANY (XNYS:GE)', 'MICROSOFT CORPORATION (XNAS:MSFT)',
           'APPLE INC. (XNAS:AAPL)']
sharpe_ratios = [0.3, 0, -0.09, 1.1, 0.7, 0.8, 0.5]
sharpe_sp500 = 0.4  # Sharpe ratio of the S&P 500

plt.figure(figsize=(10, 6))
bars = plt.bar(tickers, sharpe_ratios, color='#86bfad')

plt.axhline(y=sharpe_sp500, color='r', linestyle='--', label=f'S&P 500 Sharpe Ratio: {sharpe_sp500}')
plt.title('Sharpe Ratios (Last 3 Years) vs. S&P 500 Sharpe Ratio')
plt.xlabel('Company')
plt.ylabel('Sharpe Ratio')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

#Calculate rolling Greeks with quantstats

# Convert monthly returns to a quantstats-compatible format (Use AI to help convert for the quantstats)
portfolio_returns = qs.utils.to_returns(portfolio_data['Returns'])
benchmark_returns = qs.utils.to_returns(benchmark_data['Returns'])

# Calculate rolling alpha and beta with a 60-month window
alpha_beta_rolling = qs.stats.rolling_greeks(
    portfolio_returns,
    benchmark=benchmark_returns,
    periods=60 ).dropna()

#Plotting the beta and alpha

# Create a figure and axes for the subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Plot the rolling beta in the first panel
ax1.plot(alpha_beta_rolling['beta'], color='blue', label='Rolling Beta')
ax1.set_title('Rolling Beta (60-month)')
ax1.set_ylabel('Beta')

# Plot the rolling alpha in the second panel
ax2.plot(1200 * alpha_beta_rolling['alpha'], color='green', label='Rolling Alpha')
ax2.set_title('Rolling Alpha (60-month)')
ax2.set_xlabel('Date')
ax2.set_ylabel('Annualized Alpha (%)')


plt.tight_layout()
plt.show()
plt.savefig('Alpha&Beta')

# Fetch 10-year Treasury Bond (^TNX) data
rf = ['^TNX']
rf = yf.download(rf, start="2014-11-01", end="2024-10-31", interval='1mo', progress=False)
rf = rf.loc[:, 'Adj Close']

# Calculate the average risk-free rate
avg_rf = rf.mean()

# Print the result (convert avg_rf to a float explicitly)
print(f"The average risk-free rate: {float(avg_rf):.2f}%")


# --- Generate metrics report with Sharpe ratio ---
qs.reports.metrics(
    portfolio_returns,
    benchmark=benchmark_returns,
    rf=0.0236,  # Use the ^TNX data as the risk-free rate
    periods_per_year=12,
    prepare_returns=False,
    mode='basic'  # Use 'basic' mode to show Sharpe ratio in the console
)

IR_qs = qs.stats.information_ratio(portfolio_returns, benchmark = benchmark_returns, prepare_returns = False)

print(f"The Information ratio of our portfolio is {IR_qs:.2f}")

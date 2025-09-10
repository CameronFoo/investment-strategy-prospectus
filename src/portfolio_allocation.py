 # Sector allocations

import matplotlib.pyplot as plt #found in order to create the pie chart on chatgpt - only this line and the line plt.pie

sectors = ['Financial', 'Consumer discretionary', 'Industrial', 'Government (Bonds)', 'IT']
percentages = [17, 7, 12, 30, 34]

plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=sectors, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Industry Sector Allocation')
plt.show()

 # Sector allocations

import matplotlib.pyplot as plt #found in order to create the pie chart on chatgpt - only this line and the line plt.pie

sectors = ['Financial', 'Consumer discretionary', 'Industrial', 'Government (Bonds)', 'IT']
percentages = [17, 7, 12, 30, 34]

plt.figure(figsize=(8, 6))
plt.pie(percentages, labels=sectors, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Industry Sector Allocation')
plt.show()

#Bar chart based on the past performance
import numpy as np

tickers = ['JPMORGAN CHASE & CO. (XNYS:JPM)', 'BANK OF AMERICA CORPORATION (XNYS:BAC)', 'TESLA, INC. (XNAS:TSLA)',
           'NVIDIA CORPORATION (XNAS:NVDA)', 'GENERAL ELECTRIC COMPANY (XNYS:GE)', 'MICROSOFT CORPORATION (XNAS:MSFT)',
           'APPLE INC. (XNAS:AAPL)']
returns = [119.59, 60.38, 1487.90, 2605.36, 224.71, 191.44, 262.29]
average_return = 707.38

plt.figure(figsize=(10, 6))
bars = plt.bar(tickers, returns, color='#ff9999') #random colours used before in the pie chart

plt.axhline(y=average_return, color='r', linestyle='--', label=f'Average Return: {average_return}%')
plt.title('Past 5-Year Total Return')
plt.xlabel('Company')
plt.ylabel('5-Year Total Return (%)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

#Bar chart for the beta of each company

tickers = ['JPMORGAN CHASE & CO. (XNYS:JPM)', 'BANK OF AMERICA CORPORATION (XNYS:BAC)', 'TESLA, INC. (XNAS:TSLA)',
           'NVIDIA CORPORATION (XNAS:NVDA)', 'GENERAL ELECTRIC COMPANY (XNYS:GE)', 'MICROSOFT CORPORATION (XNAS:MSFT)',
           'APPLE INC. (XNAS:AAPL)']
betas = [1.10, 1.34, 2.36, 1.65, 1.18, 0.90, 1.23]
average_beta = np.mean(betas)  # Calculate the average beta

# Plotting the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(tickers, betas, color='#66b3ff')

plt.axhline(color='r', linestyle='--', label=f'Average Beta: {average_beta:.2f}')
plt.title('Actual Beta Values of Companies')
plt.xlabel('Company')
plt.ylabel('Beta')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
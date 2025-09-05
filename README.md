# Investment Strategy Prospectus

## Strategy Summary
This portfolio is designed for **retail investors** with a **moderate risk tolerance**.  
The objective is **capital appreciation and steady growth** through diversified exposure to equities and stable assets.  

- **70% equities** tilted towards **technology (NVIDIA, Microsoft, Tesla)** and **financials (JPMorgan, Bank of America)**  
- **Industrials (General Electric)** and **5-year U.S. Treasury bonds** provide hedges against inflation and geopolitical risk  
- **Dynamic rebalancing** is applied quarterly (or during major macroeconomic shifts) to balance growth and risk  
- Portfolio is benchmarked against the **S&P 500**  

---

## Contents

- `reports/` — Final prospectus PDF  
- `notebooks/` — Jupyter notebooks (analysis, backtests, charts)  
- `src/` — Reusable Python helpers  
- `outputs/figures/` — Generated graphs (ignore in Git)  
- `data/` — (empty) placeholder for small local datasets  

---

## Data

- All data is **publicly available** (e.g., Yahoo Finance, FRED, or equivalent APIs)  
- Data is **not stored** in this repo  
- To reproduce results:  
  1. Download from the provider or set your API key  
  2. Run the Jupyter notebooks  

---

## Environment

```bash
# Create and activate virtual environment
python -m venv .venv

# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt



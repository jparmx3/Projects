# Analysis on the magnitude of FED Target Rate changes on measures of inflation
# Created by John Armstrong 
# Goal: Looking at historical data to create consistent predictable regression model for PCE, Core PCE, CPI, Core PCI, PPI, GDP Trend

from fredapi import Fred
from dotenv import load_dotenv
import os

load_dotenv()

fred = Fred(api_key=os.getenv("FRED_API_KEY"))

fedfunds = fred.get_series('FEDFUNDS')
cpi = fred.get_series('CPIAUCSL')
core_cpi = fred.get_series('CPILFESL')
pce = fred.get_series('PCEPI')
core_pce = fred.get_series('PCEPILFE')
ppi = fred.get_series('PPIACO')
gdp = fred.get_series('GDP')

print(fedfunds.tail())
print(cpi.tail())
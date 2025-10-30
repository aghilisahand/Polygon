# =========================
# LIBRARIES
# =========================
import os, time
from dotenv import load_dotenv 
from polygon import RESTClient
from datetime import date
import pandas as pd  



# =========================
# CONFIG
# =========================

# Load environment variables from .env
load_dotenv(override=True)

# API init
apiKey = os.environ.get('POLYGON_API_KEY1')
print("API key loaded?", bool(apiKey))
client = RESTClient(apiKey)
print("Client created successfully!")





# ==========================
# CAVEMAN METHOD
# ==========================

def get_active_tickers():

	"""
	Fetch tickers for active stocks of that day
	returns a list of tickers
	"""
        
	tickers = []
	print("Fetching tickers...")

	for t in client.list_tickers(
		market="stocks",
		active="true",
		order="asc",
		limit="1000",
		sort="ticker",
		):
		tickers.append(t.ticker)
		
	print("sample:", tickers[1:5])
	return tickers


def get_aggs(timespan, symbol, start_date="2025-01-20", end_date=None):

	"""
    Fetch aggregates for a symbol and return a pandas DataFrame.
    No I/O here.
    """
	  
	aggs = []

	if end_date == None:
		end_date = str(date.today())

	# for t in tickers:
	for a in client.list_aggs(
			symbol,
			1,
			timespan,
			start_date,
			end_date,
			adjusted="true",
			sort="asc",
			limit=10000,
		): 
			aggs.append(a)

	print("sample:", aggs[1:2])

	df = pd.DataFrame(aggs)
	return df


def save_aggs_to_csv(df, filename):
    """
    Save DataFrame to CSV
    """
    if df.empty:
        print(f"No data to save for {filename}")
        return
    df.to_csv(filename, index=False)
    print(f"Saved {filename}")

def main():
	get_active_tickers()
	df = get_aggs("day", "AAPL")
	save_aggs_to_csv(df,"AAPL_day_aggs.csv")

if __name__ == "__main__":
	main()


# TODO: 1) implement error catching in my functions
#	    2) create a plan for data gathering that can lead to a meaningful analysis and possibly one i can fit a model to ?



import logging
from pathlib import Path
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
from polygon.exceptions import BadResponse



# =========================
# LOGGING
# =========================

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s",
#     datefmt="%H:%M:%S",
# )


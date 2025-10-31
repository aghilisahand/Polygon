# =========================
# LIBRARIES
# =========================

import os, time
from dotenv import load_dotenv 
from polygon import RESTClient
from datetime import date
import pandas as pd  
from pathlib import Path


# =========================
# CONFIG
# =========================

# Load environment variables from .env
load_dotenv(override=True)

# API init
apiKey = os.environ.get('POLYGON_API_KEY')
print("API key loaded?", bool(apiKey))
client = RESTClient(apiKey)
print("Client created successfully!")





# ==========================
# CAVEMAN METHOD
# ==========================


def active_tickers():

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


def save_aggs_to_csv(df: pd.DataFrame, filename: str, base_folder: str = "data", timespan: str = None, subfolder: str = "CSVS"):
    """
    Save DataFrame to CSV inside a date-first folder structure:
      <base_folder>/<YYYY-MM-DD>/<timespan>/<subfolder>/<filename>

    Example: data/2025-10-30/day/CSVS/AAPL_day_aggs.csv
    - timespan can be None -> then path is data/2025-10-30/CSVS/...
    """
    # Check DataFrame empty
    if df is None or df.empty:
        print(f"No data to save for {filename}")
        return

    today = date.today().isoformat()  # 'YYYY-MM-DD'

    # Build folder path: base_folder / today / timespan? / subfolder
    parts = [base_folder, today]
    if timespan:
        parts.append(timespan)
    if subfolder:
        parts.append(subfolder)

    folder_path = Path(*parts)
    folder_path.mkdir(parents=True, exist_ok=True)

    full_path = folder_path / filename  # filename can include .csv already
    df.to_csv(full_path, index=False)
    print(f"Saved {full_path}")

def main():

	# inits for later
	timespan = "day" ## CAN CHANGE THIS
	base_folder = "data"  # root dir for all output

    # loop over tickers, get aggs, save data
	tickers_list = active_tickers()
	for t in tickers_list:
		df = get_aggs(timespan, t)
        # pass timespan so it will be nested under the date folder
		save_aggs_to_csv(df, f"{t}_{timespan}_aggs.csv", base_folder=base_folder, timespan=timespan, subfolder="CSV's")



if __name__ == "__main__":
	main()


# TODO: 1) implement error catching in my functions
#	    2) create a plan for data gathering that can lead to a meaningful analysis and possibly one i can fit a model to ?


# =========================
# MORE LIBRARIES
# =========================



# import logging
# from pathlib import Path
# from typing import List, Tuple
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from polygon.exceptions import BadResponse



# =========================
# LOGGING
# =========================

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(message)s",
#     datefmt="%H:%M:%S",
# )


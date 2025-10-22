import os, time
from dotenv import load_dotenv 
from polygon import RESTClient
from datetime import datetime

# Load environment variables from .env
load_dotenv(override=True)

# API init
apiKey = os.environ.get('POLYGON_API_KEY1')
print("API key loaded?", bool(apiKey))
client = RESTClient(apiKey)
print("Client created successfully!")

## Get a list of tickers

tickers = []
print("Fetching tickers...")

t0 = time.time()
for t in client.list_tickers(
	market="stocks",
	active="true",
	order="asc",
	limit="1000",
	sort="ticker",
	):
    print("Fetched:", t.ticker)
    tickers.append(t.ticker)


print(len(tickers))
dt = time.time() - t0
print("time elapsed:", dt)

# TODO: I've figured out how to get a list of active tickers, I now need a practical way of grabbing daily bar data for the past couple of years and save them
# TODO: what is meant by 1 second 1 minute and 1 day bar data ? 

import os
from dotenv import load_dotenv 
from polygon import RESTClient

# Load environment variables from .env
load_dotenv()

# API init
apiKey = os.environ.get('POLYGON_API_KEY')
client = RESTClient(apiKey)

## Get a list of tickers

ticker_type = "CS" # can change this to change what kind of stock you want, we default to common stock

tickers = []
for t in client.list_tickers(
	market="stocks",
	active="true",
	order="asc",
	limit="5",
	sort="ticker",
	):
    tickers.append(t.ticker)

print(tickers)

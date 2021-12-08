import json
from utils import scraper1, scraper2

token="Insert your unique Slack token"

from slack import WebClient
client = WebClient(token=token)

header = {"User agent information"}

with open('prices.json') as f_in:
    prices = json.load(f_in)

# Webstore 1 Items
scraper("url1", header, prices, token, client)
scraper("url2", header, prices, token, client)

# Webstore 2 Items
scraper2("url1", header, prices, token, client)
scraper2("url2", header, prices, token, client)

with open('prices.json', 'w') as fp:
    json.dump(prices, fp)

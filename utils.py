import re
from bs4 import BeautifulSoup as Soup
import requests
import warnings
warnings.filterwarnings("ignore")

## You will likely have to modify this function

def scraper(url, header, prices, token, client):
    start = ## Regex start script
    end = ##Regex end script
    page = requests.get(url, headers=header)
    soup = Soup(page.text)
    title_raw = soup.find("meta", {"name":"keywords"})
    jacket = soup.find("span", {"class": "regular-price"}, strict=False)
    price_raw = jacket.find("span", {'class': 'price'}).text
    new_price = float(f"{price_raw}".replace('£', ""))

    title = re.search('%s(.*)%s' % (start, end), str(title_raw)).group(1)

    if title not in prices.keys():
        prices[title] = new_price
    elif prices[title] > new_price:
        final_price = "Price of {} has dropped from £{} to £{}".format(title, prices[title], new_price) + '\n' + "URL: {}".format(url)
        client.chat_postMessage(channel="general", text=final_price)
        prices[title] = new_price

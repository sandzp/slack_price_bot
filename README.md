## Slack Price Monitoring Bot

A simple bot that monitors the price of user-defined items at online stores. 

## To Use

### Requirements

- Beautiful Soup, Requests, Regex, Slack client
- Hickory for scheduling via command line

### Modifications

- The `utils.py` file contains the actual price monitoring function - it is likely that the items you want to monitor are not the same HTML format of the items I built this to monitor. Therefore, you would have to monitor the function to isolate the item price and title to work for the specific items you want to monitor. 

### How to use

- Once you have modified the functions in the `utils.py` file to work for the items you need (it is likely you will need to create more/less functions for the various web stores you want to monitor items on), in the `slack_price_scraper.py`file you call the individual functions and insert the URL of the item you want to monitor in the first argument of the respective function. 
- The empty `prices.json` dictionary acts as the store for the previous price point. Every time `slack_price_scraper.py` is called, it compares the latest price with the previous price (stored in the dictionary) and will send a message to your desired Slack channel if it drops below the previous price. It then updates the dictionary. If there has been no price change, then no notifications will be sent. 
- Schedule via Hickory i.e. at command line `hickory schedule slack_price_scraper3.py --every=10mins` etc. 
- Add to Slack and add token to the command in the `slack_price_scraper.py`.
- Add your browser header information (Google 'my user agent' to get this) to the header variable. 

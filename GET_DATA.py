"""
###############################################################################
            Using the Cryptocompare API to acquire historical data
###############################################################################
              
Ethan Bienstock
February 18, 2018

This file contains the code accompanying my post on acquiring historical 
cryptocurrency data using the Cryptocompare API. 

"""

import urllib
import pandas as pd
import json
from pprint import pprint

###############################################################################
# list all the exchanges
###############################################################################

url = "https://min-api.cryptocompare.com/data/all/exchanges"
with urllib.request.urlopen(url) as respone:
    all_exchanges = json.loads(respone.read())
    
print("Here are all the exchanges.")
pprint(all_exchanges.keys())

###############################################################################
# list all the exchanges# Acquire Hourly Ethereum Data
###############################################################################

coin = "ETH"
exchange = "Coinbase"
frequency = "histohour"

url = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym=USD&e={}".format(frequency,
                                                                               coin, 
                                                                               exchange)
with urllib.request.urlopen(url) as response:
    hourly_price_data = json.loads(response.read())["Data"]
    
hour_df = pd.DataFrame(hourly_price_data)
print("Hourly price data")
print(hour_df.head())

###############################################################################
# Acquire 5-Minute Litecoin Data
###############################################################################

coin = "LTC"
exchange = "Coinbase"
frequency = "histominute"
aggregate = 5

url = "https://min-api.cryptocompare.com/data/" +\
        "{}?fsym={}&tsym=USD&e={}&aggregate={}".format(frequency,
                                                       coin, 
                                                       exchange,
                                                       aggregate)

with urllib.request.urlopen(url) as response:
    minute_price_data = json.loads(response.read())["Data"]
    
five_minute_df = pd.DataFrame(minute_price_data)
print("Five minute data")
print(five_minute_df.head())

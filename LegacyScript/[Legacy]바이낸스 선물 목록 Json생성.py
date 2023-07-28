import ccxt
import json

exBN = ccxt.binanceusdm()
exBNTickersInfo = exBN.fetchTickers()
exBNTickers = exBNTickersInfo.keys()

BUSD = []
for i in exBNTickers:
    if '/' in i and '-' not in i and 'BUSD' in i:
        if '1000' in i:
            BUSD.append(i[4:-10])
        
        else:
           BUSD.append(i[0:-10])

USDT = []
for i in exBNTickers:
    if '/' in i and '-' not in i and 'USDT' in i:
        if '1000' in i:
            USDT.append(i[4:-10])
        
        else:
            USDT.append(i[0:-10])

Tickerlist = BUSD + USDT
Tickerset = set(Tickerlist)
Tickerlist = list(Tickerset)
Tickerlist.remove('BLUEBIRD')
Tickerlist.remove('BTCDOM')
Tickerlist.remove('COCOS')
Tickerlist.remove('FOOTBALL')
Tickerlist.remove('DEFI')
Tickerlist.sort()

# Create a dictionary to store the ticker list with values
ticker_dict = {}
for ticker in Tickerlist:
    # Assign a default value of None, you can change it to the desired value
    ticker_dict[ticker] = ''

# Save the dictionary as a JSON file
with open("Binance_Ticker_ids_Temp.json", "w") as json_file:
    json.dump(ticker_dict, json_file, indent=4)

print("JSON file created successfully.")
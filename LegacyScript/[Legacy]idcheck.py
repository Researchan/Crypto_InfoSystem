import requests
import ccxt
import json

url = 'https://api.coingecko.com/api/v3/coins/markets'
parameters = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 250,
    'page': 3,
}

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

Tickerlistsmall=[]
for i in Tickerlist:
    Tickerlistsmall.append((i).lower())



# Send HTTP GET request
response = requests.get(url, params=parameters)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response data in JSON format
    data = response.json()
    
    # Extract the Bitcoin price in USD
    #bitcoin_price_usd = data["bitcoin"]["usd"]
    
    iddict = {}
    for i in range(0,len(data)):
        for j in Tickerlistsmall:
            if data[i]['symbol'] == j:
                iddict[data[i]['symbol']] = data[i]['id']
    
    iddict = sorted(iddict.items())
    iddict = dict(iddict)
    for i in iddict.items():
        print(i)
else:
    print("Error:", response.status_code)
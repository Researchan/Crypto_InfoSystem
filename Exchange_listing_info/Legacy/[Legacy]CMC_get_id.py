import requests
import ccxt
import json

apikey = '339f7745-0a39-4c98-924a-39f07902c361'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apikey,
}

parameters = {
    'listing_status' : 'active',
    'start' : 1,
    'limit' : 1000,
    'sort' : 'cmc_rank',
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

iddict = {}

# Send HTTP GET request
response = requests.get(url, headers=headers, params=parameters)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response data in JSON format
    res = response.json()
    data = res['data']
    datalist = list(data)
    for i in range(0,len(datalist)):
        for j in Tickerlist:
            if datalist[i]['symbol'] == j:
                iddict[j]=datalist[i]['id']

    iddict = sorted(iddict.items())
    iddict = dict(iddict)
    for i in iddict.items():
        print(i)
    
else:
    print('error :', response.status_code, response.json())
    

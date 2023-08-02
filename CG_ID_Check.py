import requests
import ccxt
import json

url = 'https://api.coingecko.com/api/v3/coins/markets'
parameters = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 500,
    'page': 7,
}

Tickerlist = [
    "ALT", "BIOT", "BLY", "DICE", "EGG", "ENTC", "FANC", "FLZ", "GPT", "GRACY",
    "KSP", "LBL", "LM", "NPT", "OAS", "ORC", "PORTO", "REAP", "ROA", "STAT",
    "TAVA", "TEMCO", "TITAN", "TRV", "VIX", "WNCG", "XPLA", "XYM"
]

Tickerlistsmall = []
for i in Tickerlist:
    Tickerlistsmall.append(i.lower())
    
print(Tickerlistsmall)

# Send HTTP GET request
response = requests.get(url, params=parameters)

# Check if the request was successful (status code 200)
try:
    # Get the response data in JSON format
    data = response.json()
    
    # Extract the Bitcoin price in USD
    #bitcoin_price_usd = data["bitcoin"]["usd"]
    
    idlist = []
    for i in range(0,len(data)):
        for j in Tickerlistsmall:
            if data[i]['symbol'] == j:
                idlist.append(str(j) + " : " + str(data[i]['id']))
    
    idlist.sort()
    for i in idlist:
        print(i)
except:
    print("Error:", response.status_code, data)
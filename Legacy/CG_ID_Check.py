import requests
import ccxt
import json

url = 'https://api.coingecko.com/api/v3/coins/markets'
parameters = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 200,
    'page': 15,
}

Tickerlist = [
    "ABT", "AIOZ", "ALEPH", "AMPL", "AURORA", "AVT", "AXL", "BTRST", "CFG", "COVAL", "CTX", "DESO", "DEXT", "DIMO", "DYP", "ELA",
    "EUROC", "FORT", "FOX", "GFI", "GODS", "GYEN", "HOPR", "INDEX", "INV", "KRL", "LCX", "MATH", "MCO2", "MEDIA", "METIS", "MNDE",
    "MONA", "MPL", "MUSE", "ORCA", "PAX", "PLU", "PNG", "POLY", "PRIME", "PRO", "PRQ", "RARI", "RBN", "SHPING", "SPA", "SUKU",
    "SWFTC", "SYLO", "TIME", "TRAC", "VARA", "XYO"
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
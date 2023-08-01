import requests
import ccxt
import json

url = 'https://api.coingecko.com/api/v3/coins/markets'
parameters = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 500,
    'page': 2,
}

# exBN = ccxt.binanceusdm()
# exBNTickersInfo = exBN.fetchTickers()
# exBNTickers = exBNTickersInfo.keys()

# BUSD = []
# for i in exBNTickers:
#     if '/' in i and '-' not in i and 'BUSD' in i:
#         if '1000' in i:
#             BUSD.append(i[4:-10])
        
#         else:
#            BUSD.append(i[0:-10])

# USDT = []
# for i in exBNTickers:
#     if '/' in i and '-' not in i and 'USDT' in i:
#         if '1000' in i:
#             USDT.append(i[4:-10])
        
#         else:
#             USDT.append(i[0:-10])

# Tickerlist = BUSD + USDT
# Tickerset = set(Tickerlist)
# Tickerlist = list(Tickerset)
# Tickerlist.remove('BLUEBIRD')
# Tickerlist.remove('BTCDOM')
# Tickerlist.remove('COCOS')
# Tickerlist.remove('FOOTBALL')
# Tickerlist.remove('DEFI')
# Tickerlist.sort()

# Tickerlistsmall=[]
# for i in Tickerlist:
#     Tickerlistsmall.append((i).lower())

Tickerlist = [ 'CTC', 'CTSI', 'CVC', 'DAD', 'DAI', 'DAWN', 'DENT', 'DGB', 'DKA', 'DNT', 'DOGE', 'DOT', 'EGLD', 'ELF', 'ENJ', 'ENS', 'EOS', 'ETC', 'ETH', 'FCT2', 'FIL', 'FLOW', 'FOR', 'FX', 'GAL', 'GAS', 'GLM', 'GMT', 'GO', 'GRS', 'GRT', 'GTC', 'HBAR', 'HBD', 'HIFI', 'HIVE', 'HPO', 'HUNT', 'ICX', 'IMX', 'INJ', 'INTER', 'IOST', 'IOTA', 'IOTX', 'IQ', 'JST', 'JUV', 'KAVA', 'KNC', 'LINA', 'LINK', 'LOOM', 'LPT', 'LRC', 'LSK', 'MAGIC', 'MANA', 'MARO', 'MASK', 'MATIC', 'MBL', 'MED', 'META', 'MINA', 'MKR', 'MLK', 'MOC', 'MTL', 'MVL', 'NAP', 'NEAR', 'NEO', 'NKN', 'NMR', 'OBSR', 'OCEAN', 'OGN', 'ONG', 'ONIT', 'ONT', 'ORBS', 'OXT', 'PLA', 'POLYX', 'POWR', 'PROM', 'PSG', 'PUNDIX', 'QKC', 'QTCON', 'QTUM', 'RAD', 'RAY', 'REI', 'RFR', 'RLC', 'RLY', 'RNDR', 'RSR', 'RVN', 'SAND', 'SBD', 'SC', 'SHIB', 'SNT', 'SNX', 'SOL', 'SOLVE', 'SSX', 'STEEM', 'STMX', 'STORJ', 'STPT', 'STRAX', 'STRK', 'STX', 'SUI', 'SUN', 'SXP', 'T', 'TFUEL', 'THETA', 'TON', 'TRX', 'TT', 'TUSD', 'UNI', 'UPP', 'USDP', 'VAL', 'VET', 'WAVES', 'WAXP', 'XEC', 'XEM', 'XLM', 'XRP', 'XTZ', 'YGG', 'ZIL', 'ZRX']

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
    
    iddict = {}
    for i in range(0,len(data)):
        for j in Tickerlistsmall:
            #print(data[i]['symbol'],j)
            if data[i]['symbol'] == j:
                iddict[data[i]['symbol']] = data[i]['id']
    
    iddict = sorted(iddict.items())
    iddict = dict(iddict)
    for i in iddict.items():
        print(i)
except:
    print("Error:", response.status_code, data)
import ccxt
from pprint import pprint

exBN = ccxt.binanceusdm({
    'options': {
        'defaultType': 'swap',
    },
})
exBNTickersInfo = exBN.fetchTickers() # 티커 딕셔너리 가져옴
exBNTickers = exBNTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickerlist = []
for i in exBNTickers:
    if '-' not in i:
        Tickerlist.append(i[0:-10])
    
# Tickerlist.remove('DODOX')
# Tickerlist.remove('BLUEBIRD')
# Tickerlist.remove('BTCDOM')
# Tickerlist.remove('COCOS')
# Tickerlist.remove('FOOTBALL')
# Tickerlist.remove('DEFI')

# Tickerlist.append('DODO')
Tickerlist.sort()

print(Tickerlist)
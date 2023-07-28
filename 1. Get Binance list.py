import ccxt
from pprint import pprint

exBN = ccxt.binanceusdm()
exBNTickersInfo = exBN.fetchTickers() # 티커 딕셔너리 가져옴
exBNTickers = exBNTickersInfo.keys() # 티커 키만 받아오기 (이름만)


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

Tickerlist = BUSD+USDT
Tickerset = set(Tickerlist)
Tickerlist = list(Tickerset)
Tickerlist.remove('BLUEBIRD')
Tickerlist.remove('BTCDOM')
Tickerlist.remove('COCOS')
Tickerlist.remove('FOOTBALL')
Tickerlist.remove('DEFI')
Tickerlist.sort()

for i in Tickerlist:
    print(i)
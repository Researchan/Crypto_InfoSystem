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
    if '-' not in i and '/BTC' not in i: #BTC선물페어와, Delivery선물페어 정리
        Tickerlist.append(i[0:-10])
        # Tickerlist.append(i)

Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)

#ETF 삭제, 잘못된 페어이름 삭제
Tickerlist.remove('DODOX')
Tickerlist.remove('BLUEBIRD')
Tickerlist.remove('BTCDOM')
Tickerlist.remove('COCOS')
Tickerlist.remove('FOOTBALL')
Tickerlist.remove('DEFI')

#단위작은 페어 삭제후 재 등록.
Tickerlist.remove('1000FLOKI')
Tickerlist.append('FLOKI')
Tickerlist.remove('1000LUNC')
Tickerlist.append('LUNC')
Tickerlist.remove('1000PEPE')
Tickerlist.append('PEPE')
Tickerlist.remove('1000SHIB')
Tickerlist.append('SHIB')
Tickerlist.remove('1000XEC')
Tickerlist.append('XEC')

Tickerlist.sort()

# for i in Tickerlist:
#     print(i)
import ccxt

exBN = ccxt.binance({
    'options': {
        'defaultType': 'spot',
    },
})
exBNTickersInfo = exBN.fetchTickers() # 티커 딕셔너리 가져옴
exBNTickers = exBNTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickerlist = []
for i in exBNTickers:
    Tickerlist.append(i)

Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()
import ccxt
from pprint import pprint

exBybit = ccxt.bybit({
    'options': {
        'defaultType': 'swap',
    },
})
exBybitTickersInfo = exBybit.fetchTickers() # 티커 딕셔너리 가져옴
exBybitTickers = exBybitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickerlist = []
for i in exBybitTickers:
    if '/' in i and '-' not in i and 'USDT' in i:
            if '1000' not in i:
                Tickerlist.append(i[0:-10])

Tickerset = set(Tickerlist)
Tickerlist = list(Tickerset)
Tickerlist.append('LADYS')
Tickerlist.append('NFT')
Tickerlist.append('BONK')
Tickerlist.append('BTT')
Tickerlist.append('FLOKI')
Tickerlist.append('LUNC')
Tickerlist.append('PEPE')
Tickerlist.append('SHIB')
Tickerlist.append('XEC')
Tickerlist.sort()


# for i in Tickerlist:
#     print(i)

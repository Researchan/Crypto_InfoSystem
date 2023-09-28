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
    if 'USDC' not in i: # USDC페어는 제외.
        Tickerlist.append(i[0:-10])
        # Tickerlist.append(i)

Tickerlist.remove('10000LADYS')
Tickerlist.remove('10000NFT')
Tickerlist.remove('1000BONK')
Tickerlist.remove('1000BTT')
Tickerlist.remove('1000FLOKI')
Tickerlist.remove('1000LUNC')
Tickerlist.remove('1000PEPE')
Tickerlist.remove('1000XEC')
Tickerlist.remove('SHIB1000')

Tickerlist.append('LADYS')
Tickerlist.append('NFT')
Tickerlist.append('BONK')
Tickerlist.append('BTT')
Tickerlist.append('FLOKI')
Tickerlist.append('LUNC')
Tickerlist.append('PEPE')
Tickerlist.append('SHIB')
Tickerlist.append('XEC')

Tickerset = set(Tickerlist)
Tickerlist = list(Tickerset)
Tickerlist.sort()

# print(Tickerlist)
for i in Tickerlist:
    print(i)

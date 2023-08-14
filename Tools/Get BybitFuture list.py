import ccxt
from pprint import pprint

exBybit = ccxt.bybit({
    'apiKey':'',
    'secret':'',
    'enableRateLimit' : False,
    'options': {
        'defaultType': 'swap',
    },
})
exBybitTickersInfo = exBybit.fetchTickers() # 티커 딕셔너리 가져옴
exBybitTickers = exBybitTickersInfo.keys() # 티커 키만 받아오기 (이름만)


# BUSD = []
# for i in exBNTickers:
#     if '/' in i and '-' not in i and 'BUSD' in i:
#         if '1000' in i:
#             BUSD.append(i[4:-10])
        
#         else:
#            BUSD.append(i[0:-10])

Tickerlist = []
for i in exBybitTickers:
    if '/' in i and '-' not in i and 'USDT' in i:
        if '1000' not in i:
            Tickerlist.append(i[0:-10])
        
        # else:
        #     Tickerlist.append(i[0:-10])
            
# for i in exBybitTickers:
#     if '/' in i and '-' not in i and 'USDT' in i:
#         if '1000' in i:
#             print(i)
#             #USDT.append(i[4:-10])

Tickerset = set(Tickerlist)
Tickerlist = list(Tickerset)
# Tickerlist.remove('BLUEBIRD')
# Tickerlist.remove('BTCDOM')
# Tickerlist.remove('COCOS')
# Tickerlist.remove('FOOTBALL')
# Tickerlist.remove('DEFI')
Tickerlist.sort()

for i in Tickerlist:
    print(i)

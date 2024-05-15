import ccxt

exBN = ccxt.binanceusdm({
    'options': {
        'defaultType': 'swap',
    },
})
exBNTickersInfo = exBN.fetchTickers() # 티커 딕셔너리 가져옴
exBNTickers = exBNTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickerlist = []
for i in exBNTickers:
    if '-' not in i and ':USDT' in i: #BTC선물페어와, Delivery선물페어 정리
        Tickerlist.append(i[0:-10])

Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)

#ETF 삭제, 잘못된 페어이름 삭제
Tickerlist.remove('COCOS/USDT:USDT')
Tickerlist.remove('DEFI/USDT:USDT')
Tickerlist.remove('BLUEBIRD/USDT:USDT')
Tickerlist.remove('FOOTBALL/USDT:USDT')
Tickerlist.remove('BTCDOM/USDT:USDT')
Tickerlist.remove('TOMO/USDT:USDT')
Tickerlist.remove('RAD/USDT:USDT')
Tickerlist.remove('ANT/USDT:USDT')
Tickerlist.remove('CTK/USDT:USDT')
Tickerlist.remove('DGB/USDT:USDT')
Tickerlist.remove('STPT/USDT:USDT')
Tickerlist.remove('STRAX/USDT:USDT')

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
Tickerlist.remove('1000BONK')
Tickerlist.append('BONK')
Tickerlist.remove('1000SATS')
Tickerlist.append('SATS')
Tickerlist.remove('1000RATS')
Tickerlist.append('RATS')

#DODO티커 정리
Tickerlist.remove('DODOX')
Tickerlist.append('DODO')

# BEAM티커 정리
Tickerlist.remove('BEAMX')
Tickerlist.append('BEAM')

# TOMO 리브랜딩 후 VIC 미상장
Tickerlist.remove('TOMO')
# Tickerlist.append('VIC')

Tickerlist.sort()

# for i in Tickerlist:
#     print(i)
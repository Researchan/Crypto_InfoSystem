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
# Tickerlist.remove('BLUEBIRD')
Tickerlist.remove('BTCDOM')
# Tickerlist.remove('COCOS')
# Tickerlist.remove('FOOTBALL')
Tickerlist.remove('DEFI')
# Tickerlist.remove('TOMO') #TOMO가 VIC으로 바뀜. C98이 인수. 근데 합병은 안했네. 그리고 선물 미상장
Tickerlist.remove('RAD')
# Tickerlist.remove('ANT')
Tickerlist.remove('CTK')
Tickerlist.remove('DGB')
Tickerlist.remove('STPT')
Tickerlist.remove('STRAX')
Tickerlist.remove('CVX')
# Tickerlist.remove('MBL')
Tickerlist.remove('MDT')
# Tickerlist.remove('AUDIO')
Tickerlist.remove('SLP')
Tickerlist.remove('IDEX')
Tickerlist.remove('SNT')
Tickerlist.remove('GLMR')
Tickerlist.remove('WAVES')
Tickerlist.remove('AGIX') #AGIX 상폐
Tickerlist.remove('OCEAN') #OCEAN 상폐

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

# RON티커 정리
Tickerlist.remove('RONIN')
Tickerlist.append('RON')

#RNDR 티커 정리/
# Tickerlist.remove('RNDR')
# Tickerlist.append('RENDER')


Tickerlist.sort()

# for i in Tickerlist:
#     print(i)
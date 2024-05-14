import ccxt
import time

exBNfuture = ccxt.binanceusdm({
    'options': {
        'defaultType': 'swap',
    },
})
exBNfutureTickersInfo = exBNfuture.fetchTickers() # 티커 딕셔너리 가져옴
exBNfutureTickers = exBNfutureTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickerlist = []
for i in exBNfutureTickers:
    if '-' not in i and ':USDT' in i:
        Tickerlist.append(i)

Tickerlist.remove('COCOS/USDT:USDT')
Tickerlist.remove('DEFI/USDT:USDT')
Tickerlist.remove('BLUEBIRD/USDT:USDT')
Tickerlist.remove('FOOTBALL/USDT:USDT')
Tickerlist.remove('BTCDOM/USDT:USDT')
Tickerlist.remove('TOMO/USDT:USDT')
Tickerlist.sort()


#OI Dict 생성 및 저장
OI_Dict ={}

for i in Tickerlist:
    try:
        res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
            'limit':'1',
        })
        # print(res)
        #현재 OI

        OI_Dict[str(i)] = round(res[0]['openInterestValue'])
    except Exception as e:
        print(res)
        break

New_OI_Dict = {}

#페어 이름정보 변경 (자동)
for key, value in OI_Dict.items():
    new_key = key[0:-10]
    New_OI_Dict[new_key] = value
    
# #페어 이름정보 변경 (수동)
# New_OI_Dict['DODO'] = New_OI_Dict.pop('DODOX')
New_OI_Dict['FLOKI'] = New_OI_Dict.pop('1000FLOKI')
New_OI_Dict['LUNC'] = New_OI_Dict.pop('1000LUNC')
New_OI_Dict['PEPE'] = New_OI_Dict.pop('1000PEPE')
New_OI_Dict['SHIB'] = New_OI_Dict.pop('1000SHIB')
New_OI_Dict['XEC'] = New_OI_Dict.pop('1000XEC')
New_OI_Dict['SATS'] = New_OI_Dict.pop('1000SATS')
New_OI_Dict['RATS'] = New_OI_Dict.pop('1000RATS')
New_OI_Dict['BONK'] = New_OI_Dict.pop('1000BONK')
# New_OI_Dict['BEAM'] = New_OI_Dict.pop('BEAMX') #C98 리브랜딩
# New_OI_Dict['VIC'] = New_OI_Dict.pop('TOMO') #토모 리브랜딩

#OI 내림차순
sorted_OI_Dict = dict(sorted(New_OI_Dict.items(), key=lambda x: x[1], reverse=True) )

# for i in sorted_OI_Dict:
#     print(i)
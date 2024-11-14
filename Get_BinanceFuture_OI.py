import ccxt
import time
import jandimodule

# try:
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

# Tickerlist.remove('COCOS/USDT:USDT')
Tickerlist.remove('DEFI/USDT:USDT')
# Tickerlist.remove('BLUEBIRD/USDT:USDT')
# Tickerlist.remove('FOOTBALL/USDT:USDT')
Tickerlist.remove('BTCDOM/USDT:USDT')
# Tickerlist.remove('TOMO/USDT:USDT')
Tickerlist.remove('RAD/USDT:USDT')
# Tickerlist.remove('ANT/USDT:USDT')
Tickerlist.remove('CTK/USDT:USDT')
Tickerlist.remove('DGB/USDT:USDT')
Tickerlist.remove('STPT/USDT:USDT')
Tickerlist.remove('STRAX/USDT:USDT')
Tickerlist.remove('CVX/USDT:USDT')
# Tickerlist.remove('MBL/USDT:USDT')
Tickerlist.remove('MDT/USDT:USDT')
# Tickerlist.remove('AUDIO/USDT:USDT')
Tickerlist.remove('SLP/USDT:USDT')
Tickerlist.remove('IDEX/USDT:USDT')
Tickerlist.remove('SNT/USDT:USDT')
Tickerlist.remove('GLMR/USDT:USDT')
Tickerlist.remove('WAVES/USDT:USDT')
Tickerlist.remove('AGIX/USDT:USDT') #AGIX 상폐
Tickerlist.remove('OCEAN/USDT:USDT') #OCEAN 상폐
Tickerlist.remove('UNFI/USDT:USDT') #UNFI 상폐
Tickerlist.sort()


#OI Dict 생성 및 저장
OI_Dict ={}

for i in Tickerlist:
    res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
        'limit':'1',
    })
    OI_Dict[str(i)] = round(res[0]['openInterestValue'])
    
    # OI정보 보내주지 않는 페어는 오류나게 됨.
    # print(i, ' : ', OI_Dict[str(i)])

New_OI_Dict = {}

#페어 이름정보 변경 (자동)
for key, value in OI_Dict.items():
    new_key = key[0:-10]
    New_OI_Dict[new_key] = value
    
# #페어 이름정보 변경 (수동)
New_OI_Dict['FLOKI'] = New_OI_Dict.pop('1000FLOKI')
New_OI_Dict['LUNC'] = New_OI_Dict.pop('1000LUNC')
New_OI_Dict['PEPE'] = New_OI_Dict.pop('1000PEPE')
New_OI_Dict['SHIB'] = New_OI_Dict.pop('1000SHIB')
New_OI_Dict['XEC'] = New_OI_Dict.pop('1000XEC')
New_OI_Dict['SATS'] = New_OI_Dict.pop('1000SATS')
New_OI_Dict['RATS'] = New_OI_Dict.pop('1000RATS')
New_OI_Dict['BONK'] = New_OI_Dict.pop('1000BONK')
New_OI_Dict['MOG'] = New_OI_Dict.pop('1000000MOG')
New_OI_Dict['X'] = New_OI_Dict.pop('1000X')
New_OI_Dict['DODO'] = New_OI_Dict.pop('DODOX') #DODO 바낸 페어 이름.
New_OI_Dict['BEAM'] = New_OI_Dict.pop('BEAMX') #MeritCircle 리브랜딩
New_OI_Dict['RON'] = New_OI_Dict.pop('RONIN') #MeritCircle 리브랜딩
# New_OI_Dict['RENDER'] = New_OI_Dict.pop('RNDR') #RNDR 리브랜딩
# New_OI_Dict['VIC'] = New_OI_Dict.pop('TOMO') #토모 리브랜딩했는데 선물상장 안해줌.
New_OI_Dict['BABYDOGE'] = New_OI_Dict.pop('1MBABYDOGE') # BABYDOGE 정리

#OI 내림차순
sorted_OI_Dict = dict(sorted(New_OI_Dict.items(), key=lambda x: x[1], reverse=True) )

# for i in sorted_OI_Dict:
#     print(i)
        
# except Exception as e:
#     print(e)
#     jandimodule.Exchange_Listing_send_message_to_jandi(str(e) + ' BinanceFuture_OI 오류')
import ccxt

#1 인스턴스 생성
exBNfuture = ccxt.binanceusdm({
    'options': {
        'defaultType': 'swap',
    },
})

#2 티커 딕셔너리 가져옴
exBNfutureTickersInfo = exBNfuture.fetchTickers()

#3 티커 키만 받아오기 (이름만)
exBNTickers = exBNfutureTickersInfo.keys()

#4 티커 BTC페어, Deilvery선물 제거
Tickerlist = []
for i in exBNTickers:
    if '-' not in i and ':USDT' in i:
        Tickerlist.append(i)
        
Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)

#5 잘못되거나 제외할 페어이름 삭제
Tickerlist.remove('DEFI/USDT:USDT')
Tickerlist.remove('BTCDOM/USDT:USDT')
Tickerlist.remove('RAD/USDT:USDT')
Tickerlist.remove('CTK/USDT:USDT')
Tickerlist.remove('DGB/USDT:USDT')
Tickerlist.remove('STPT/USDT:USDT')
Tickerlist.remove('STRAX/USDT:USDT')
Tickerlist.remove('CVX/USDT:USDT')
Tickerlist.remove('MDT/USDT:USDT')
Tickerlist.remove('SLP/USDT:USDT')
Tickerlist.remove('IDEX/USDT:USDT')
Tickerlist.remove('SNT/USDT:USDT')
Tickerlist.remove('GLMR/USDT:USDT')
Tickerlist.remove('WAVES/USDT:USDT')
Tickerlist.remove('AGIX/USDT:USDT')
Tickerlist.remove('OCEAN/USDT:USDT')
Tickerlist.remove('UNFI/USDT:USDT')
Tickerlist.remove('KLAY/USDT:USDT')
Tickerlist.remove('REN/USDT:USDT')
Tickerlist.remove('KEY/USDT:USDT')
Tickerlist.remove('BOND/USDT:USDT')
Tickerlist.sort()


#6 OI Dict 및 새롭게 티커 바꿔서 저장할 New Dict 생성
OI_Dict ={}
New_OI_Dict = {}

#7 OI정보 받아와서 저장.
for i in Tickerlist:
    res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
        'limit':'1',
    })
    OI_Dict[str(i)] = round(res[0]['openInterestValue'])
    
    # OI정보 보내주지 않는 페어는 오류나게 됨.
    # print(i, ' : ', OI_Dict[str(i)])

#8 OI정보 저장된 곳 티커 정리하기
for key, value in OI_Dict.items():
    new_key = key[0:-10]
    New_OI_Dict[new_key] = value


#9 티커 리스트 업데이트

New_Tickerlist = []
for i in Tickerlist:
    New_Tickerlist.append(i[0:-10])

New_Tickerlist = set(New_Tickerlist)
New_Tickerlist = list(New_Tickerlist)


#단위작은 페어 삭제후 재 등록. (수동)
New_OI_Dict['FLOKI'] = New_OI_Dict.pop('1000FLOKI')
New_Tickerlist.remove('1000FLOKI')
New_Tickerlist.append('FLOKI')

New_OI_Dict['LUNC'] = New_OI_Dict.pop('1000LUNC')
New_Tickerlist.remove('1000LUNC')
New_Tickerlist.append('LUNC')

New_OI_Dict['PEPE'] = New_OI_Dict.pop('1000PEPE')
New_Tickerlist.remove('1000PEPE')
New_Tickerlist.append('PEPE')

New_OI_Dict['SHIB'] = New_OI_Dict.pop('1000SHIB')
New_Tickerlist.remove('1000SHIB')
New_Tickerlist.append('SHIB')

New_OI_Dict['XEC'] = New_OI_Dict.pop('1000XEC')
New_Tickerlist.remove('1000XEC')
New_Tickerlist.append('XEC')

New_OI_Dict['BONK'] = New_OI_Dict.pop('1000BONK')
New_Tickerlist.remove('1000BONK')
New_Tickerlist.append('BONK')

New_OI_Dict['SATS'] = New_OI_Dict.pop('1000SATS')
New_Tickerlist.remove('1000SATS')
New_Tickerlist.append('SATS')

New_OI_Dict['RATS'] = New_OI_Dict.pop('1000RATS')
New_Tickerlist.remove('1000RATS')
New_Tickerlist.append('RATS')

New_OI_Dict['CAT'] = New_OI_Dict.pop('1000CAT')
New_Tickerlist.remove('1000CAT')
New_Tickerlist.append('CAT')

New_OI_Dict['MOG'] = New_OI_Dict.pop('1000000MOG')
New_Tickerlist.remove('1000000MOG')
New_Tickerlist.append('MOG')

New_OI_Dict['X'] = New_OI_Dict.pop('1000X')
New_Tickerlist.remove('1000X')
New_Tickerlist.append('X')

New_OI_Dict['CHEEMS'] = New_OI_Dict.pop('1000CHEEMS')
New_Tickerlist.remove('1000CHEEMS')
New_Tickerlist.append('CHEEMS')

New_OI_Dict['WHY'] = New_OI_Dict.pop('1000WHY')
New_Tickerlist.remove('1000WHY')
New_Tickerlist.append('WHY')

New_OI_Dict['DODO'] = New_OI_Dict.pop('DODOX')  #도도 바낸 특이
New_Tickerlist.remove('DODOX')
New_Tickerlist.append('DODO')

New_OI_Dict['BEAM'] = New_OI_Dict.pop('BEAMX') #메리트 서클
New_Tickerlist.remove('BEAMX')
New_Tickerlist.append('BEAM')

New_OI_Dict['RON'] = New_OI_Dict.pop('RONIN')
New_Tickerlist.remove('RONIN')
New_Tickerlist.append('RON')

New_OI_Dict['BABYDOGE'] = New_OI_Dict.pop('1MBABYDOGE')
New_Tickerlist.remove('1MBABYDOGE')
New_Tickerlist.append('BABYDOGE')

New_OI_Dict['RAY'] = New_OI_Dict.pop('RAYSOL') #레이디움은 왜 바이낸스도 바이비트도 다 티커가 다를까.
New_Tickerlist.remove('RAYSOL')
New_Tickerlist.append('RAY')

New_Tickerlist.sort()
Tickerlist = New_Tickerlist

#OI 내림차순
sorted_OI_Dict = dict(sorted(New_OI_Dict.items(), key=lambda x: x[1], reverse=True) )

# for i in Tickerlist:
#     print(i)

# for i in sorted_OI_Dict:
#     print(i)
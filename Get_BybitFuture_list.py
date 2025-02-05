import ccxt

exBybit = ccxt.bybit({
    'options': {
        'defaultType': 'swap',
    },
})
exBybitTickersInfo = exBybit.fetchTickers() # 티커 딕셔너리 가져옴
exBybitTickers = exBybitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

#1 Bybit 티커 받아오기 (USDC, Deilivery, ETF 제거)
Tickerlist = []
for i in exBybitTickers:
    if 'USDT:USDT' in i:
        Tickerlist.append(i)
    #print(i)

#2 잘못된 티커, 조회 안되는 티커, 조회 안할 티커 삭제
# Tickerlist.remove('SPEC/USDT:USDT') # 코마캡에없음, 생겨서 넣음
Tickerlist.remove('ETHBTC/USDT:USDT') # 인덱스
# Tickerlist.remove('DOP1/USDT:USDT') # 코개코에 없음, 근데 이젠 상폐당함. 그래서 안지워도 됨.
# Tickerlist.remove('MAX/USDT:USDT') # 코개코에 없음, 생겨서 넣음.
# Tickerlist.remove('HPOS10I/USDT:USDT') # 코개코 코마캡에는 BITCOIN으로 되어있는데, 헷갈릴까봐 이런 이름으로 상장하는듯함.
# Tickerlist.remove('ME/USDT:USDT') # 코개코 없음 매직에덴. 이젠 생겼으니 다시 넣기.
# Tickerlist.remove('BIO/USDT:USDT') # 코개코 없음 PRE마켓인데 왜 잡히지?
        
#마지막 가격정보 불러오기
lastprices = exBybit.fetch_tickers(Tickerlist)

#OI 딕셔너리 생성
Bybit_OI_Dict ={}
Bybit_New_OI_Dict = {}

#원하는 티커에 대해서 OI정보 받아오기 + 가격 * OIvolume = USD Value 계산.
for i in Tickerlist:
    res = exBybit.fetch_open_interest_history(i, timeframe='5m', params={ 
            'limit':'1',
        })
    #print(i)
    Bybit_OI_Dict[i] = round(lastprices[i]['last'] * res[0]['openInterestValue'])
    # print(res)

#OI Dice에서 이름 형식 정리.
for key, value in Bybit_OI_Dict.items():
    new_key = key[0:-10]
    Bybit_New_OI_Dict[new_key] = value

New_Tickerlist = []
for i in Tickerlist:
    New_Tickerlist.append(i[0:-10])

New_Tickerlist = set(New_Tickerlist)
New_Tickerlist = list(New_Tickerlist)

# 티커 형식 정리
Bybit_New_OI_Dict['LADYS'] = Bybit_New_OI_Dict.pop('10000LADYS')
New_Tickerlist.remove('10000LADYS')
New_Tickerlist.append('LADYS')

Bybit_New_OI_Dict['BONK'] = Bybit_New_OI_Dict.pop('1000BONK')
New_Tickerlist.remove('1000BONK')
New_Tickerlist.append('BONK')

Bybit_New_OI_Dict['BTT'] = Bybit_New_OI_Dict.pop('1000BTT')
New_Tickerlist.remove('1000BTT')
New_Tickerlist.append('BTT')

Bybit_New_OI_Dict['FLOKI'] = Bybit_New_OI_Dict.pop('1000FLOKI')
New_Tickerlist.remove('1000FLOKI')
New_Tickerlist.append('FLOKI')

Bybit_New_OI_Dict['LUNC'] = Bybit_New_OI_Dict.pop('1000LUNC')
New_Tickerlist.remove('1000LUNC')
New_Tickerlist.append('LUNC')

Bybit_New_OI_Dict['PEPE'] = Bybit_New_OI_Dict.pop('1000PEPE')
New_Tickerlist.remove('1000PEPE')
New_Tickerlist.append('PEPE')

Bybit_New_OI_Dict['SHIB'] = Bybit_New_OI_Dict.pop('SHIB1000')
New_Tickerlist.remove('SHIB1000')
New_Tickerlist.append('SHIB')

Bybit_New_OI_Dict['XEC'] = Bybit_New_OI_Dict.pop('1000XEC')
New_Tickerlist.remove('1000XEC')
New_Tickerlist.append('XEC')

Bybit_New_OI_Dict['SATS'] = Bybit_New_OI_Dict.pop('10000SATS')
New_Tickerlist.remove('10000SATS')
New_Tickerlist.append('SATS')

Bybit_New_OI_Dict['RATS'] = Bybit_New_OI_Dict.pop('1000RATS')
New_Tickerlist.remove('1000RATS')
New_Tickerlist.append('RATS')

Bybit_New_OI_Dict['WEN'] = Bybit_New_OI_Dict.pop('10000WEN')
New_Tickerlist.remove('10000WEN')
New_Tickerlist.append('WEN')

Bybit_New_OI_Dict['TURBO'] = Bybit_New_OI_Dict.pop('1000TURBO')
New_Tickerlist.remove('1000TURBO')
New_Tickerlist.append('TURBO')

Bybit_New_OI_Dict['AIDOGE'] = Bybit_New_OI_Dict.pop('10000000AIDOGE')
New_Tickerlist.remove('10000000AIDOGE')
New_Tickerlist.append('AIDOGE')

Bybit_New_OI_Dict['COQ'] = Bybit_New_OI_Dict.pop('10000COQ')
New_Tickerlist.remove('10000COQ')
New_Tickerlist.append('COQ')

Bybit_New_OI_Dict['MOG'] = Bybit_New_OI_Dict.pop('1000000MOG')
New_Tickerlist.remove('1000000MOG')
New_Tickerlist.append('MOG')

Bybit_New_OI_Dict['BABYDOGE'] = Bybit_New_OI_Dict.pop('1000000BABYDOGE')
New_Tickerlist.remove('1000000BABYDOGE')
New_Tickerlist.append('BABYDOGE')

Bybit_New_OI_Dict['APU'] = Bybit_New_OI_Dict.pop('1000APU')
New_Tickerlist.remove('1000APU')
New_Tickerlist.append('APU')

Bybit_New_OI_Dict['PEIPEI'] = Bybit_New_OI_Dict.pop('1000000PEIPEI')
New_Tickerlist.remove('1000000PEIPEI')
New_Tickerlist.append('PEIPEI')

Bybit_New_OI_Dict['CAT'] = Bybit_New_OI_Dict.pop('1000CAT') #캣츠랑 헷갈려
New_Tickerlist.remove('1000CAT')
New_Tickerlist.append('CAT')

Bybit_New_OI_Dict['NEIRO'] = Bybit_New_OI_Dict.pop('1000NEIROCTO')
New_Tickerlist.remove('1000NEIROCTO') #바낸 표준 맞춰서 NEIRO로 바꿀 것.
New_Tickerlist.append('NEIRO')

Bybit_New_OI_Dict['MUMU'] = Bybit_New_OI_Dict.pop('1000MUMU')
New_Tickerlist.remove('1000MUMU')
New_Tickerlist.append('MUMU')

Bybit_New_OI_Dict['WHY'] = Bybit_New_OI_Dict.pop('10000WHY')
New_Tickerlist.remove('10000WHY')
New_Tickerlist.append('WHY')

Bybit_New_OI_Dict['CATS'] = Bybit_New_OI_Dict.pop('1000CATS') #캣이랑 헷갈려
New_Tickerlist.remove('1000CATS')
New_Tickerlist.append('CATS')

Bybit_New_OI_Dict['X'] = Bybit_New_OI_Dict.pop('1000X')
New_Tickerlist.remove('1000X')
New_Tickerlist.append('X')

Bybit_New_OI_Dict['CHEEMS'] = Bybit_New_OI_Dict.pop('1000000CHEEMS')
New_Tickerlist.remove('1000000CHEEMS')
New_Tickerlist.append('CHEEMS')

Bybit_New_OI_Dict['TOSHI'] = Bybit_New_OI_Dict.pop('1000TOSHI')
New_Tickerlist.remove('1000TOSHI')
New_Tickerlist.append('TOSHI')

Bybit_New_OI_Dict['RAY'] = Bybit_New_OI_Dict.pop('RAYDIUM') #바이낸스 바이비트 다 문제야
New_Tickerlist.remove('RAYDIUM')
New_Tickerlist.append('RAY')

Bybit_New_OI_Dict['QUBIC'] = Bybit_New_OI_Dict.pop('10000QUBIC') #바이낸스 바이비트 다 문제야
New_Tickerlist.remove('10000QUBIC')
New_Tickerlist.append('QUBIC')

# 코마캡에 없어서 잠시 보류했는데, 몇달째 없는 줄 알았더니 이거 그냥 RIF인데 바이비트가 기상장 코인이랑 티커 겹쳐서 못넣는중. 
Bybit_New_OI_Dict['RIF'] = Bybit_New_OI_Dict.pop('RIFSOL') #바이낸스 바이비트 다 문제야
New_Tickerlist.remove('RIFSOL')
New_Tickerlist.append('RIF')


New_Tickerlist.sort()
Tickerlist = New_Tickerlist


#OI 내림차순
sorted_OI_Dict = dict(sorted(Bybit_New_OI_Dict.items(), key=lambda item: item[1], reverse=True))

# for i in Tickerlist:
#     print(i)

# for i in sorted_OI_Dict:
#     print(i)


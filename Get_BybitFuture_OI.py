import ccxt

exBybit = ccxt.bybit({
    'options': {
        'defaultType': 'swap',
    },
})
exBybitTickersInfo = exBybit.fetchTickers() # 티커 딕셔너리 가져옴
exBybitTickers = exBybitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

#Bybit 티커 조정
Tickerlist = []
for i in exBybitTickers:
    if 'USDT:USDT' in i:
        Tickerlist.append(i)

# print(Tickerlist)

#마지막 가격정보 불러오기
lastprices = exBybit.fetch_tickers(Tickerlist)

#OI 딕셔너리 생성
Bybit_OI_Dict ={}

for i in Tickerlist:
    #원하는 티커에 대해서 OI정보 받아오기
    res = exBybit.fetch_open_interest_history(i, timeframe='5m', params={ 
            'limit':'1',
        })
    
    #가격정보 받아서 OIvolume과 곱해서 USD value 계산 후 Dict에 집어넣기
    Bybit_OI_Dict[i] = round(lastprices[i]['last'] * res[0]['openInterestValue']) 

Bybit_New_OI_Dict = {}

#페어 이름정보 변경 (자동)
for key, value in Bybit_OI_Dict.items():
    new_key = key[0:-10]
    Bybit_New_OI_Dict[new_key] = value

#페어 이름정보 변경 (수동)
Bybit_New_OI_Dict['LADYS'] = Bybit_New_OI_Dict.pop('10000LADYS')
Bybit_New_OI_Dict['NFT'] = Bybit_New_OI_Dict.pop('10000NFT')
Bybit_New_OI_Dict['BONK'] = Bybit_New_OI_Dict.pop('1000BONK')
Bybit_New_OI_Dict['BTT'] = Bybit_New_OI_Dict.pop('1000BTT')
Bybit_New_OI_Dict['FLOKI'] = Bybit_New_OI_Dict.pop('1000FLOKI')
Bybit_New_OI_Dict['LUNC'] = Bybit_New_OI_Dict.pop('1000LUNC')
Bybit_New_OI_Dict['PEPE'] = Bybit_New_OI_Dict.pop('1000PEPE')
Bybit_New_OI_Dict['SHIB'] = Bybit_New_OI_Dict.pop('SHIB1000')
Bybit_New_OI_Dict['XEC'] = Bybit_New_OI_Dict.pop('1000XEC')
Bybit_New_OI_Dict['STARL'] = Bybit_New_OI_Dict.pop('10000STARL')
Bybit_New_OI_Dict['SATS'] = Bybit_New_OI_Dict.pop('10000SATS')
Bybit_New_OI_Dict['RATS'] = Bybit_New_OI_Dict.pop('1000RATS')
Bybit_New_OI_Dict['WEN'] = Bybit_New_OI_Dict.pop('10000WEN')
Bybit_New_OI_Dict['TURBO'] = Bybit_New_OI_Dict.pop('1000TURBO')
Bybit_New_OI_Dict['AIDOGE'] = Bybit_New_OI_Dict.pop('10000000AIDOGE')
Bybit_New_OI_Dict['COQ'] = Bybit_New_OI_Dict.pop('10000COQ')
# Bybit_New_OI_Dict['IQ50'] = Bybit_New_OI_Dict.pop('1000IQ50')
Bybit_New_OI_Dict['MOG'] = Bybit_New_OI_Dict.pop('1000000MOG')
Bybit_New_OI_Dict['BEER'] = Bybit_New_OI_Dict.pop('1000BEER')
Bybit_New_OI_Dict['BABYDOGE'] = Bybit_New_OI_Dict.pop('1000000BABYDOGE')
Bybit_New_OI_Dict['APU'] = Bybit_New_OI_Dict.pop('1000APU')
Bybit_New_OI_Dict['PEIPEI'] = Bybit_New_OI_Dict.pop('1000000PEIPEI')

#OI 내림차순
sorted_OI_Dict = dict(sorted(Bybit_New_OI_Dict.items(), key=lambda item: item[1], reverse=True))
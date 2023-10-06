import ccxt
import time
from jandimodule import *

exBybitFuture = ccxt.bybit({
    'options': {
        'defaultType': 'swap',
    },
})
exBybitTickersInfo = exBybitFuture.fetchTickers() # 티커 딕셔너리 가져옴
exBybitTickers = exBybitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

#Bybit 티커 조정
Tickerlist = []
for i in exBybitTickers:
    if 'USD:USDC' not in i:
        Tickerlist.append(i)

#마지막 가격정보 불러오기
lastprices = exBybitFuture.fetch_tickers(Tickerlist)

#OI 딕셔너리 생성
Bybit_OI_Dict ={}

#원하는 티커에 대해서 OI정보 받아오기, 마지막 가격 딕셔너리에넣기, 계산하기
for i in Tickerlist:
    res = exBybitFuture.fetch_open_interest_history(i, timeframe='5m', params={
            'limit':'1',
        })
    
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

#OI 내림차순
sorted_OI_Dict = dict(sorted(Bybit_New_OI_Dict.items(), key=lambda item: item[1], reverse=True))

# OI 순위 메세지 전송
count = 1
formatted_message = ''
for key,value in list(sorted_OI_Dict.items())[0:200]:
    coin = key
    OIvolume = '${:,.0f}'.format(value)
    formatted_line = f'{coin}\n{OIvolume}\n\n'
    formatted_message += (str(count)+ '. ' + formatted_line)
    count += 1
formatted_message = '***Bybit_OI***\n\n' + formatted_message
formatted_message = formatted_message.rstrip()
Bybit_OI_Alert_send_message_to_jandi(formatted_message)

formatted_message = ''
for key,value in list(sorted_OI_Dict.items())[200:]:
    coin = key
    OIvolume = '${:,.0f}'.format(value)
    formatted_line = f'{coin}\n{OIvolume}\n\n'
    formatted_message += (str(count)+ '. ' + formatted_line)
    count += 1
formatted_message = formatted_message.rstrip()
Bybit_OI_Alert_send_message_to_jandi(formatted_message)
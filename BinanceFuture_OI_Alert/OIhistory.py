import ccxt 
import time

exBNfuture = ccxt.binanceusdm()
exBNfutureTickersInfo = exBNfuture.fetchTickers() # 티커 딕셔너리 가져옴
exBNfutureTickers = exBNfutureTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickers = []
for i in exBNfutureTickers:
    if '-' not in i and 'USDT' in i:
        Tickers.append(i[0:-5])
    
Tickers.remove('COCOS/USDT')
Tickers.sort()

OI_Dict ={}
for i in Tickers:
    time.sleep(0.1)
    
    try:
        res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
            'limit':'1',
        })
        print(i, " OpenInterest : ", res[0]['openInterestValue'])
        OI_Dict[str(i)] = res
        
    except Exception as e:
        print(i, ':', str(e))
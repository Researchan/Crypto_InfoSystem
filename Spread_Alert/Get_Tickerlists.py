import ccxt
import Get_BinanceBybitTicker

exBNfuture = ccxt.binanceusdm()
exBNfutureTickersInfo = exBNfuture.fetchTickers() # 티커 딕셔너리 가져옴
exBNfutureTickers = exBNfutureTickersInfo.keys() # 티커 키만 받아오기 (이름만)

USDT = []
for i in exBNfutureTickers:
    if '/' in i and '-' not in i and 'USDT' in i:
        USDT.append(i[0:-5])
            
        if '1000' in i:
            USDT.remove(i[0:-5])
            

Tickerlist = USDT

Tickerlist.remove('BLUEBIRD/USDT')
Tickerlist.remove('BTCDOM/USDT')
Tickerlist.remove('COCOS/USDT')
Tickerlist.remove('FOOTBALL/USDT')
Tickerlist.remove('DEFI/USDT')
Tickerlist.remove('LUNA2/USDT') #루나는 따로참조
Tickerlist.sort()


future1000_Tickerlist = ['1000FLOKI/USDT', '1000LUNC/USDT', '1000PEPE/USDT', '1000SHIB/USDT', '1000XEC/USDT']
Luna_Tickerlist = ['LUNA/USDT', 'LUNA2/USDT']
Binance_Bybit_diff_Tickers = Get_BinanceBybitTicker.Tickerlist
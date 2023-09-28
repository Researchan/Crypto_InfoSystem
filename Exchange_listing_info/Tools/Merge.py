import Get_BinanceFuture_list
import Get_Bithumb_list
import Get_BybitFuture_list
import Get_Upbit_BTC_list
import Get_Upbit_KRW_list

Upbit_BTC = Get_Upbit_BTC_list.Tickerlist
Upbit_KRW = Get_Upbit_KRW_list.Tickerlist
Binance = Get_BinanceFuture_list.Tickerlist
Bybit = Get_BybitFuture_list.Tickerlist
Bithumb = Get_Bithumb_list.Tickerlist

Coin_list = Upbit_BTC + Upbit_KRW + Binance + Bybit + Bithumb
Coin_list = set(Coin_list)
Coin_list = list(Coin_list)
Coin_list.sort()

for i in Coin_list:
    print(i)

Coin_Infos = {}

# Coin_Infos['1inch'] = {
#     'upbit':None,
#     'bithumb':None,
#     'binance':None,
#     'bybit':None
# }
# testdict['1inch']['upbit'] = 'O'
# testdict['1inch']['bithumb'] = 'O'
# testdict['1inch']['binance'] = 'O'
# testdict['1inch']['bybit'] = 'X'

# print(testdict)
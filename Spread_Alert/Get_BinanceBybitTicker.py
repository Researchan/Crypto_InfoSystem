import Get_BinanceFuture_list
import Get_BybitFuture_list
import Get_BinanceSpot_list

BinanceFuture_list = Get_BinanceFuture_list.Tickerlist
BinanceSpot_list = Get_BinanceSpot_list.Tickerlist
BybitFuture_list = Get_BybitFuture_list.Tickerlist

BinanceFuture_list = set(BinanceFuture_list)
BybitFuture_list = set(BybitFuture_list)

Only_Bybit_Future_list = BybitFuture_list - BinanceFuture_list

Only_Bybit_Future_list = list(Only_Bybit_Future_list)

Only_Bybit_Future_list.sort()

# print(Only_Bybit_Future_list)
# print(BinanceSpot_list)

Tickerlist = []

for i in BinanceSpot_list:
    for j in Only_Bybit_Future_list:
        if (str(j)+'/') in i:
            Tickerlist.append(j+'/USDT:USDT')
            


Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)


Tickerlist.remove('BTT/USDT:USDT') #BTT는 1000Pairs라 또 제거
Tickerlist.sort()
import Get_BinanceFuture_list
import Get_Bithumb_list
import Get_BybitFuture_list
import Get_Upbit_list

Upbit_List = Get_Upbit_list.Upbittickers
Bithumb_List = Get_Bithumb_list.tickerlist
BinanceFuture_list = Get_BinanceFuture_list.Tickerlist
BybitFuture_list = Get_BybitFuture_list.Tickerlist

Every_Tickers_List = Upbit_List+Bithumb_List+BinanceFuture_list+BybitFuture_list
Every_Tickers_sets = set(Every_Tickers_List)
Every_Tickers_List = list(Every_Tickers_sets)
Every_Tickers_List.append('TON(Tokamak)')
Every_Tickers_List.remove('TRV')
Every_Tickers_List.remove('GRACY')
Every_Tickers_List.sort()

# print(Every_Tickers_List)
for i in Every_Tickers_List:
    print(i)
import Get_BinanceFuture_list
import Get_Bithumb_list
import Get_BybitFuture_list
import Get_Upbit_BTC_list
import Get_Upbit_KRW_list

Upbit_BTC_list = Get_Upbit_BTC_list.Tickerlist
Upbit_KRW_list = Get_Upbit_KRW_list.Tickerlist
Binance_Future_list = Get_BinanceFuture_list.Tickerlist
Bybit_Future_list = Get_BybitFuture_list.Tickerlist
Bithumb_list = Get_Bithumb_list.Tickerlist

# 각 거래소 상장리스트 합산하여 전체 리스트 생성 및 정렬
Coin_list = Upbit_KRW_list + Upbit_BTC_list + Binance_Future_list + Bybit_Future_list + Bithumb_list
Coin_list = set(Coin_list)
Coin_list = list(Coin_list)
Coin_list.sort()

# 전체 정보를 담을 딕셔너리 생성
Coin_Infos = {}

for i in Coin_list:
    Coin_Infos[i] = {
        'Upbit_KRW':None,
        'Upbit_BTC':None,
        'Bithumb':None,
        'Binance_Future':None,
        'Bybit_Future':None
    }
    
    if i in Upbit_KRW_list:
        Coin_Infos[i]['Upbit_KRW'] = 'O'
    elif i not in Upbit_KRW_list:
        Coin_Infos[i]['Upbit_KRW'] = 'X'
        
    if i in Upbit_BTC_list:
        Coin_Infos[i]['Upbit_BTC'] = 'O'
    elif i not in Upbit_BTC_list:
        Coin_Infos[i]['Upbit_BTC'] = 'X'
        
    if i in Binance_Future_list:
        Coin_Infos[i]['Binance_Future'] = 'O'
    elif i not in Binance_Future_list:
        Coin_Infos[i]['Binance_Future'] = 'X'
        
    if i in Bybit_Future_list:
        Coin_Infos[i]['Bybit_Future'] = 'O'
    elif i not in Bybit_Future_list:
        Coin_Infos[i]['Bybit_Future'] = 'X'
        
    if i in Bithumb_list:
        Coin_Infos[i]['Bithumb'] = 'O'    
    elif i not in Bithumb_list:
        Coin_Infos[i]['Bithumb'] = 'X'
import pyupbit

#업비트 KRW 마켓 티커들 반환
def Get_UpbitKRW_Tickers():
    KRWmarket_list = []
    KRWtickers = pyupbit.get_tickers(fiat="KRW")

    for i in KRWtickers:
        KRWmarket_list.append(i[4:])
    
    KRWmarket_list.sort()    
    return KRWmarket_list

#업비트 BTC 마켓 티커들 반환
def Get_UpbitBTC_Tickers():
    BTCmarket_list = []
    BTCtickers = pyupbit.get_tickers(fiat="BTC")

    for i in BTCtickers:
        BTCmarket_list.append(i[4:])

    BTCmarket_list.sort()
    return BTCmarket_list

#업비트 모든 상장코인 티커 반환
def Get_UpbitAll_Tickers():
    Allmarket_list = Get_UpbitKRW_Tickers() + Get_UpbitBTC_Tickers()
    temp = set(Allmarket_list)
    Allmarket_list = list(temp)

    Allmarket_list.sort()
    return Allmarket_list

Upbittickers = Get_UpbitKRW_Tickers()

# print(Upbittickers)
for ticker in Upbittickers:
    print(ticker)
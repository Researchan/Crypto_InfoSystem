import ccxt

exUpbit = ccxt.upbit({})
exUpbitTickersInfo = exUpbit.fetchTickers() # 티커 딕셔너리 가져옴
exUpbitTickers = exUpbitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickerlist = []
for i in exUpbitTickers:
    if '/KRW' in i:
        Tickerlist.append(i[0:-4])
        
Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()

# print(Tickerlist)
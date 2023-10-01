import ccxt

exUpbit = ccxt.upbit({})
exUpbitTickersInfo = exUpbit.fetchTickers() # 티커 딕셔너리 가져옴
exUpbitTickers = exUpbitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

Tickerlist = []
for i in exUpbitTickers:
    if '/KRW' in i:
        Tickerlist.append(i[0:-4])

# Tokamak이 TON이랑 겹침. 또한 오름차순 정렬시 소문자 O를 엑셀이 구분하기때문에 전부 대문자로 변경

Tickerlist.remove('Tokamak Network')
Tickerlist.append('TOKAMAK NETWORK')
Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()

# for i in Tickerlist:
#     print(i)
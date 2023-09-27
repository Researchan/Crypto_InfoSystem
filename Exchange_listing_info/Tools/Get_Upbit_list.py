import ccxt

exUpbit = ccxt.upbit({})
exUpbitTickersInfo = exUpbit.fetchTickers() # 티커 딕셔너리 가져옴
exUpbitTickers = exUpbitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

BTClist = []
KRWlist = []
Alllist = []
for i in exUpbitTickers:
    if i[-3:] == 'BTC':
        BTClist.append(i[0:-4])
    elif i[-3:] == 'KRW':
        KRWlist.append(i[0:-4])
        
Alllist = BTClist + KRWlist
# Alllist = set(Alllist)
# Alllist = list(Alllist)
# Alllist.sort()

# BTClist.remove()
# KRWlist.remove()

print(Alllist)
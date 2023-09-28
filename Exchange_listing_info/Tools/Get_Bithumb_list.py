import ccxt

exBithumb = ccxt.bithumb({})
exBithumbTickersInfo = exBithumb.fetchTickers() # 티커 딕셔너리 가져옴
exBithumbTickers = exBithumbTickersInfo.keys() # 티커 키만 받아오기 (이름만)

BTClist = []
KRWlist = []
Tickerlist = []
for i in exBithumbTickers:
    if i[-3:] == 'BTC':
        BTClist.append(i[0:-4])
    elif i[-3:] == 'KRW':
        KRWlist.append(i[0:-4])
        
Tickerlist = BTClist + KRWlist

Tickerlist.remove('ArchLoot')
Tickerlist.append('ALT')
Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()


# print(Tickerlist)
for i in Tickerlist:
    print(i)
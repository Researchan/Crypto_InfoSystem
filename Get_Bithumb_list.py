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

#아치루트 제거후 ALT로 변경
Tickerlist.remove('ArchLoot')
Tickerlist.append('ALT')

#AXL 티커 조정
Tickerlist.remove('WAXL')
Tickerlist.append('AXL')

#GRACY는 제거. 코마캡 코개코도 상장안된 잡페어
Tickerlist.remove('GRACY')
Tickerlist.remove('USDT')

#PLA 해킹 마이그레이션 PDA 잠시 지우기.
# Tickerlist.remove('PDA')

Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()


# for i in Tickerlist:
#     print(i)
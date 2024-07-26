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
# Tickerlist.remove('ArchLoot')
# Tickerlist.append('ALT')

#AXL 티커 조정
Tickerlist.remove('WAXL')
Tickerlist.append('AXL')

#RNDR 티커 정리/
Tickerlist.remove('RNDR')
Tickerlist.append('RENDER')

#코마캡 코개코도 상장안된 잡페어
Tickerlist.remove('LWA')
Tickerlist.remove('GRACY')
Tickerlist.remove('USDT')
Tickerlist.remove('XENT') # ENTC 리브랜딩. 안나옴 제외.

Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()


# for i in Tickerlist:
#     print(i)
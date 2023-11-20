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

#GRACY는 제거. 코마캡 코개코도 상장안된 잡페어
Tickerlist.remove('GRACY')

#상장초기라 코인마캣캡 상장이 안되어있네. 코개코만있다.
Tickerlist.remove('ZTX')

Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()


# for i in Tickerlist:
#     print(i)
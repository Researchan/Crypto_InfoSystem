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
Tickerlist.append('AL')

#AXL 티커 조정
Tickerlist.remove('WAXL')
Tickerlist.append('AXL')

#RNDR 티커 정리/
# Tickerlist.remove('RNDR')
# Tickerlist.append('RENDER')

#코마캡 코개코도 상장안된 잡페어
Tickerlist.remove('LWA')
# Tickerlist.remove('GRACY') 빗썸단독상장 개잡코, 코마캡 코개코 생겨서 넣음.
Tickerlist.remove('USDT')
# Tickerlist.remove('XENT') # ENTC 리브랜딩. 안나옴 제외. /결국 상폐당함
Tickerlist.remove('FLZ') #빗썸 단독상장 개잡코인데 FDV 3B 이라서 짜증나서 제외함. 어차피 재단만 갖고있는 쓰레기
# Tickerlist.remove('HPO') 
# Tickerlist.remove('HP') #업비트랑 둘만 상장된 김치. 정보도 잘 없어서 제외

Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)
Tickerlist.sort()


# for i in Tickerlist:
#     print(i)
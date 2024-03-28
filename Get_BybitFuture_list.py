import ccxt

exBybit = ccxt.bybit({
    'options': {
        'defaultType': 'swap',
    },
})
exBybitTickersInfo = exBybit.fetchTickers() # 티커 딕셔너리 가져옴
exBybitTickers = exBybitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

#Bybit 티커 조정
Tickerlist = []
for i in exBybitTickers:
    if 'USDT:USDT' in i:
        Tickerlist.append(i[0:-10])

# 단위 작은 티커 제거
Tickerlist.remove('10000LADYS')
Tickerlist.remove('10000NFT')
Tickerlist.remove('1000BONK')
Tickerlist.remove('1000BTT')
Tickerlist.remove('1000FLOKI')
Tickerlist.remove('1000LUNC')
Tickerlist.remove('1000PEPE')
Tickerlist.remove('1000XEC')
Tickerlist.remove('SHIB1000')
Tickerlist.remove('10000STARL')
Tickerlist.remove('10000SATS')
Tickerlist.remove('1000RATS')
Tickerlist.remove('10000WEN')
Tickerlist.remove('1000TURBO')
Tickerlist.remove('10000000AIDOGE')
Tickerlist.remove('10000COQ')
Tickerlist.remove('1000IQ50')

#이거 코개코에 없어서 삭제
Tickerlist.remove('PUNDU')

#SCA 코개코없네.
Tickerlist.remove('SCA')

# 제거한 티커 표준맞춰서 다시 추가
Tickerlist.append('LADYS')
Tickerlist.append('NFT')
Tickerlist.append('BONK')
Tickerlist.append('BTT')
Tickerlist.append('FLOKI')
Tickerlist.append('LUNC')
Tickerlist.append('PEPE')
Tickerlist.append('SHIB')
Tickerlist.append('XEC')
Tickerlist.append('STARL')
Tickerlist.append('SATS')
Tickerlist.append('RATS')
Tickerlist.append('WEN')
Tickerlist.append('TURBO')
Tickerlist.append('AIDOGE')
Tickerlist.append('COQ')
Tickerlist.append('IQ50')

Tickerset = set(Tickerlist)
Tickerlist = list(Tickerset)
Tickerlist.sort()

# for i in Tickerlist:
#     print(i)


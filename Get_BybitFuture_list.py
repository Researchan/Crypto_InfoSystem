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


Tickerlist.remove('SPEC') # 코마캡에없음
Tickerlist.remove('ETHBTC') # 인덱스
Tickerlist.remove('DOP1') # 코개코에 없음
Tickerlist.remove('MAX') # 코개코에 없음
Tickerlist.remove('HPOS10I') # 코개코 코마캡 둘 다 없네.
Tickerlist.remove('UNFI') # 이거 왜 바빗 계속 보내주냐..

# 단위 작은 티커 제거
Tickerlist.remove('10000LADYS')
# Tickerlist.remove('10000NFT') #상폐
Tickerlist.remove('1000BONK')
Tickerlist.remove('1000BTT')
Tickerlist.remove('1000FLOKI')
Tickerlist.remove('1000LUNC')
Tickerlist.remove('1000PEPE')
Tickerlist.remove('1000XEC')
Tickerlist.remove('SHIB1000')
# Tickerlist.remove('10000STARL') #상폐
Tickerlist.remove('10000SATS')
Tickerlist.remove('1000RATS')
Tickerlist.remove('10000WEN')
Tickerlist.remove('1000TURBO')
Tickerlist.remove('10000000AIDOGE')
Tickerlist.remove('10000COQ')
# Tickerlist.remove('1000IQ50') 상폐.
Tickerlist.remove('1000000MOG')
# Tickerlist.remove('1000BEER') # 갓비트 컷ㅋㅋ 상폐 개좆같은 MM새끼들 ㅋㅋ
Tickerlist.remove('1000000BABYDOGE')
Tickerlist.remove('1000APU')
Tickerlist.remove('1000000PEIPEI')
Tickerlist.remove('1000CAT')
Tickerlist.remove('1000NEIROCTO') #바낸 표준 맞춰서 NEIRO로 바꿀 것.
Tickerlist.remove('1000MUMU') #바낸 표준 맞춰서 NEIRO로 바꿀 것.
Tickerlist.remove('10000WHY') #솔직히 이런 억지밈코 상장 지겹다 이젠.
Tickerlist.remove('1000CATS')
Tickerlist.remove('1000X')


# 제거한 티커 표준맞춰서 다시 추가
Tickerlist.append('LADYS')
# Tickerlist.append('NFT') # 상폐
Tickerlist.append('BONK')
Tickerlist.append('BTT')
Tickerlist.append('FLOKI')
Tickerlist.append('LUNC')
Tickerlist.append('PEPE')
Tickerlist.append('SHIB')
Tickerlist.append('XEC')
# Tickerlist.append('STARL') #상폐
Tickerlist.append('SATS')
Tickerlist.append('RATS')
Tickerlist.append('WEN')
Tickerlist.append('TURBO')
Tickerlist.append('AIDOGE')
Tickerlist.append('COQ')
# Tickerlist.append('IQ50') #상폐
Tickerlist.append('MOG')
# Tickerlist.append('BEER')
Tickerlist.append('BABYDOGE')
Tickerlist.append('APU')
Tickerlist.append('PEIPEI')
Tickerlist.append('CAT')
Tickerlist.append('NEIRO')
Tickerlist.append('MUMU')
Tickerlist.append('WHY')
Tickerlist.append('CATS')
Tickerlist.append('X')


Tickerset = set(Tickerlist)
Tickerlist = list(Tickerset)
Tickerlist.sort()

# for i in Tickerlist:
#     print(i)


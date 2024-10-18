import ccxt
#코베가 API키 방식이 달라져서 그냥  포기했음. 원래도 귀찮았는데 대응 안하는 쪽으로 선회.

exCB = ccxt.coinbase({
    'apiKey':'a04f8779-d954-4dff-8bf5-a2bdbd7d2a15',
    'secret':'MHcCAQEEIGzMb0JHOdgbly25JWS2bdJ320QPc3BIdzYNqoi2IIZuoAoGCCqGSM49\nAwEHoUQDQgAE7Mgf4E2BglxD5PX13DPb7Bt77wgKBH6ix6JSfDN0eEH0CXjtiTzu\nV34nsJn3+s/eKEegZQmZKa0hR8wJTxx2jg==',
    'options': {
        'defaultType': 'spot',
    },
})
exCBTickersInfo = exCB.fetch_tickers() # 티커 딕셔너리 가져옴
exCBTickers = exCBTickersInfo.keys() # 티커 키만 받아오기 (이름만)

#API에서 USD 존재하는 페어의 티커만 받아오기
Tickerlist = []

for i in exCBTickers:
    if '/USD' in i:
        word = i.split('/')[0]
        Tickerlist.append(word)
        
Tickerlist = set(Tickerlist)
Tickerlist = list(Tickerlist)

Tickerlist.remove('00')
Tickerlist.remove('USDT')
Tickerlist.remove('WBTC')
Tickerlist.remove('PYUSD')
Tickerlist.remove('MSOL')
Tickerlist.remove('LSETH')
Tickerlist.remove('GUSD')
Tickerlist.remove('CBETH')
Tickerlist.remove('BIT')
# Tickerlist.remove('EUROC') #유로
Tickerlist.remove('EURC') #유로
Tickerlist.remove('PAX') # 너무 잡코라 그냥 삭제
Tickerlist.remove('WAXL') # AXL 랩핑한 거 삭제. (AXL은 기본적으로 있기 때문에 추가안해도 됨)
# Tickerlist.remove('RENDER') # RNDR랑 같은 토큰인데 ERC말고 솔라나는 이름을 다르게해서 상장해버렸네. 제거함... 은 다른애들도 마이그레이션.
Tickerlist.remove('RNDR')
Tickerlist.remove('KARRAT') #뭐야 이 잡코는..

# 센트리퓨지는 랩핑토큰제거하고 원래토큰으로 저장.
Tickerlist.remove('WCFG')
Tickerlist.append('CFG')

# AMPL은 랩핑토큰제거하고 원래토큰으로 저장.
# Tickerlist.remove('WAMPL')
Tickerlist.append('AMPL')

# RONIN티커 정리
Tickerlist.remove('RONIN')
Tickerlist.append('RON')

# CORE 티커 정리
Tickerlist.remove('CORECHAIN')
Tickerlist.append('CORE')
    
#정렬
Tickerlist.sort()



# for i in Tickerlist:
#     print(i)
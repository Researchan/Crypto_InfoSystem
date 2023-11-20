import ccxt

exCB = ccxt.coinbase({
    'apiKey':'Eg0muGsS6RHoh7fV',
    'secret':'Ruqp7i61bWeZ783FYTmOFa1dUfDsjasT',
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
Tickerlist.remove('EUROC') #유로
Tickerlist.remove('PAX') # 너무 잡코라 그냥 삭제
Tickerlist.remove('WAXL') # AXL 랩핑한 거 삭제. (AXL은 기본적으로 있기 때문에 추가안해도 됨)

# 센트리퓨지는 랩핑토큰제거하고 원래토큰으로 저장.
Tickerlist.remove('WCFG')
Tickerlist.append('CFG')

# 센트리퓨지는 랩핑토큰제거하고 원래토큰으로 저장.
Tickerlist.remove('WAMPL')
Tickerlist.append('AMPL')
    
#정렬
Tickerlist.sort()


# for i in Tickerlist:
#     print(i)
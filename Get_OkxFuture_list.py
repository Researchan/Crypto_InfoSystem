import ccxt
import SlackModule

try:
    exOkx = ccxt.okx({
        'options': {
            'defaultType': 'swap',
        },
    })
    exOkxTickersInfo = exOkx.fetchTickers() # 티커 딕셔너리 가져옴
    exOkxTickers = exOkxTickersInfo.keys() # 티커 키만 받아오기 (이름만)

    Tickerlist = []
    for i in exOkxTickers:
        if '/USDT:USDT' in i:
            coin = i.split('/')[0]
            Tickerlist.append(coin)

    Tickerset = set(Tickerlist)
    Tickerlist = list(Tickerset)

    # 상폐됐는데 API에서 여전히 주고있는 코인이름 삭제 - 다 익명성 관련이네
    # 231221 이제 제대로 삭제됐네
    # Tickerlist.remove('DASH') 
    # Tickerlist.remove('ZEN')
    # Tickerlist.remove('ZEC')
    # Tickerlist.remove('XMR')

    #이거 코개코에서 등록될떄까지 냅둔다.
    # Tickerlist.remove('BLOCK') #코개코가 등록해줬으니 차단해제.
    # Tickerlist.remove('MAX') # 코개코에 없음. 생김
    # Tickerlist.remove('PI') # CG에 없어서 보류.
    Tickerlist.remove('XAUT') # 금이라서 제외


    # 루나 이름 통일
    Tickerlist.remove('LUNA')
    Tickerlist.append('LUNA2')

    Tickerlist.sort()


    # for i in Tickerlist:
    #     print(i)

except Exception as e:
    error_message = f"OKX Future 데이터 수집 중 오류 발생: {str(e)}"
    print(error_message)
    SlackModule.Exchange_Listing_send_message_to_slack(error_message)
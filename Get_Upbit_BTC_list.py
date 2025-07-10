import ccxt
import SlackModule

Tickerlist = []  # 모듈 레벨에서 Tickerlist 변수 정의

try:
    exUpbit = ccxt.upbit({})
    
    # 모든 티커를 한 번에 가져오지 않고, BTC 마켓만 가져옵니다
    markets = exUpbit.load_markets()
    for symbol in markets:
        if symbol.endswith('/BTC'):
            ticker = symbol.split('/')[0]
            Tickerlist.append(ticker)
    
    # 제외할 토큰 목록
    tokens_to_remove = [
        'USDT',  # 테더
        'OCEAN',  # 삭제
        'GAME2',  # CoinGecko에 정보없음
        'HP',  # 쓰레기 컷
    ]
    
    # 제외된 토큰 출력
    # print("\n제외된 토큰 목록:")
    # for token in sorted(tokens_to_remove):
    #     if token in Tickerlist:
    #         print(f"- {token}")
    
    # 토큰 제거
    for token in tokens_to_remove:
        if token in Tickerlist:
            Tickerlist.remove(token)
    
    # 중복 제거 및 정렬
    Tickerlist = set(Tickerlist)
    Tickerlist = list(Tickerlist)
    Tickerlist.sort()
    
    # print(f"\n총 {len(Tickerlist)}개의 BTC 페어가 있습니다:")
    # for ticker in Tickerlist:
    #     print(ticker)
    
except Exception as e:
    error_message = f"업비트 BTC 데이터 수집 중 오류 발생: {str(e)}"
    print(error_message)
    SlackModule.Exchange_Listing_send_message_to_slack(error_message)
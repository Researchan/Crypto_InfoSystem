import ccxt
import SlackModule

try:
    exUpbit = ccxt.upbit({})
    # 모든 심볼 가져오기
    all_symbols = exUpbit.load_markets().keys()
    # KRW 페어만 필터링
    krw_symbols = [symbol for symbol in all_symbols if '/KRW' in symbol]

    # 심볼 목록을 여러 개의 작은 그룹으로 나누기
    chunk_size = 100
    symbol_chunks = [krw_symbols[i:i + chunk_size] for i in range(0, len(krw_symbols), chunk_size)]

    Tickerlist = []
    for chunk in symbol_chunks:
        # 각 그룹에 대해 fetchTickers() 메서드 호출
        tickers_info = exUpbit.fetch_tickers(chunk)
        for i in tickers_info.keys():
            Tickerlist.append(i[0:-4])

    # Tokamak이 TON이랑 겹침. 또한 오름차순 정렬시 소문자 O를 엑셀이 구분하기때문에 전부 대문자로 변경
    #Tickerlist.remove('Tokamak Network')
    #Tickerlist.append('TOKAMAK')

    Tickerlist.remove('GAME2') #CoinGecko에 정보없음.
    Tickerlist.remove('USDT') #테더삭제
    Tickerlist.remove('HP')
    # Tickerlist.remove('BOUNTY') #코개코랑 코마캡에 없음 생김.

    Tickerlist = set(Tickerlist)
    Tickerlist = list(Tickerlist)
    Tickerlist.sort()

    # print(f"\n총 {len(Tickerlist)}개의 KRW 페어가 있습니다:")
    # for i in Tickerlist:
    #     print(i)

except Exception as e:
    error_message = f"업비트 데이터 수집 중 오류 발생: {str(e)}"
    print(error_message)
    SlackModule.Exchange_Listing_send_message_to_slack(error_message)
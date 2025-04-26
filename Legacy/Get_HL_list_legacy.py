import ccxt
import jandimodule
import time

try:
    # HyperLiquid 거래소 객체 생성
    exHL = ccxt.hyperliquid({
        'options': {
            'defaultType': 'swap',  # 선물 시장으로 설정
        },
    })
    
    # 마켓 데이터 로드
    print("마켓 데이터 로드 중...")
    markets = exHL.load_markets()
    time.sleep(1)  # API 제한 방지를 위한 대기
    
    # 선물 페어만 필터링 (USDC 페어)
    all_symbols = []
    for symbol in markets.keys():
        if ':USDC' in symbol:  # USDC 페어만 선택
            all_symbols.append(symbol)
    
    print(f"총 {len(all_symbols)}개의 페어가 발견되었습니다.")
    
    # 실제 거래가능한 페어 확인
    print("\n거래 가능 여부 확인 중...")
    
    # 거래 가능 여부를 확인하기 위해 틱 데이터 가져오기
    tickers_info = exHL.fetch_tickers()
    time.sleep(1)  # API 제한 방지를 위한 대기
    
    # 활성화된 페어 목록 생성
    active_symbols = []
    delisted_symbols = []
    
    for symbol, ticker_data in tickers_info.items():
        if ':USDC' in symbol:
            # 24시간 거래량을 확인하여 거래 가능 여부 판단
            volume = ticker_data['quoteVolume'] if 'quoteVolume' in ticker_data else 0
            last_price = ticker_data['last'] if 'last' in ticker_data and ticker_data['last'] else 0
            is_active = ticker_data['active'] if 'active' in ticker_data else None
            
            # 거래량이 있거나 가격이 있거나 active 플래그가 True인 경우 활성화된 페어로 간주
            if volume > 0 or last_price > 0 or is_active == True:
                active_symbols.append(symbol)
            else:
                delisted_symbols.append(symbol)
    
    # 상장폐지된 페어 목록 출력
    if delisted_symbols:
        print(f"\n상장폐지된 페어 목록 (총 {len(delisted_symbols)}개):")
        for symbol in delisted_symbols[:10]:  # 처음 10개만 출력
            coin = symbol.split('/')[0]
            if ':' in coin:
                coin = coin.split(':')[0]
            print(coin)
        
        if len(delisted_symbols) > 10:
            print(f"... 외 {len(delisted_symbols) - 10}개")
    else:
        print("\n상장폐지된 페어가 없습니다.")
    
    # 활성화된 페어만 필터링
    Symbollist = active_symbols
    
    print(f"\n활성화된 페어 수: {len(Symbollist)}개")
    
    # 마지막 가격정보 불러오기
    print("\n가격 정보 로드 중...")
    lastprices = exHL.fetch_tickers(Symbollist)
    time.sleep(1)  # API 제한 방지를 위한 대기
    
    # OI 딕셔너리 생성
    HL_OI_Dict = {}
    
    print("\nOI 정보 수집 중...")
    print("(처리 시간이 다소 걸릴 수 있습니다...)")
    
    # 처리 상태 표시 변수
    total_count = len(Symbollist)
    processed_count = 0
    success_count = 0
    
    # OI 정보 수집
    for symbol in Symbollist:
        processed_count += 1
        if processed_count % 5 == 0:  # 5개 처리할 때마다 상태 출력
            print(f"진행 중: {processed_count}/{total_count} ({int(processed_count/total_count*100)}%)...")
        
        try:
            # OI 정보 가져오기
            oi_data = exHL.fetch_open_interest(symbol)
            time.sleep(1)  # API 제한 방지를 위한 대기
            
            if oi_data and 'openInterestAmount' in oi_data:
                # USD 가치 계산 (OI * 마지막 가격)
                if symbol in lastprices and 'last' in lastprices[symbol] and lastprices[symbol]['last']:
                    price = lastprices[symbol]['last']
                    # openInterestAmount 사용
                    oi_amount = oi_data.get('openInterestAmount', 0)
                    if oi_amount:  # None이 아닌 경우에만 계산
                        oi_value = oi_amount * price
                        # 심볼에서 코인명 추출
                        coin = symbol.split('/')[0]
                        if ':' in coin:
                            coin = coin.split(':')[0]
                        HL_OI_Dict[coin] = int(oi_value)  # int 사용
                        success_count += 1
        except Exception as e:
            # 오류는 상세하게 기록하지 않고 무시
            pass
    
    print(f"\nOI 정보 수집 완료: {success_count}/{total_count} 성공")
    
    # 코인명만 추출하여 Tickerlist 생성
    Tickerlist = list(HL_OI_Dict.keys())
    
    # 알파벳 순으로 정렬
    Tickerlist.sort()
    
    # 페어 목록 출력
    print(f"\nHyperLiquid 활성화된 선물 페어 목록 (총 {len(Tickerlist)}개):")
    for ticker in Tickerlist[:30]:  # 처음 30개만 출력
        print(ticker, end=', ')
    
    if len(Tickerlist) > 30:
        print(f"... 외 {len(Tickerlist) - 30}개")
    else:
        print()
    
    # OI 내림차순 정렬
    sorted_OI_Dict = dict(sorted(HL_OI_Dict.items(), key=lambda x: x[1], reverse=True))
    
    # 모든 OI 출력
    print("\nHyperLiquid 모든 페어의 OI:")
    for ticker, oi in sorted_OI_Dict.items():
        print(f"{ticker}: ${oi:,}")
    
    # 전체 OI 합계
    total_oi = sum(sorted_OI_Dict.values())
    print(f"\n전체 OI 합계: ${total_oi:,}")
    
except Exception as e:
    error_message = f"HyperLiquid 데이터 수집 중 오류 발생: {str(e)}"
    print(error_message)
    jandimodule.Exchange_Listing_send_message_to_jandi(error_message) 
import ccxt
import SlackModule
import time

# 다른 파일에서 import할 변수
Tickerlist = []
sorted_OI_Dict = {}

try:
    print("HyperLiquid 데이터 수집 시작 (빠른 버전)...")
    
    # HyperLiquid 거래소 객체 생성
    exHL = ccxt.hyperliquid({
        'options': {
            'defaultType': 'swap',  # 선물 시장으로 설정
        },
    })
    
    # 마켓 데이터 로드
    print("마켓 데이터 로드 중...")
    markets = exHL.load_markets()
    
    # 선물 페어만 필터링 (USDC 페어)
    all_symbols = []
    for symbol in markets.keys():
        if ':USDC' in symbol:  # USDC 페어만 선택
            all_symbols.append(symbol)
    
    print(f"총 {len(all_symbols)}개의 페어가 발견되었습니다.")
    
    # 활성 페어 확인을 위한 틱 데이터 가져오기
    print("\n거래 가능 여부 확인 중...")
    tickers_info = exHL.fetch_tickers()
    
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
    symbol_list = active_symbols
    print(f"\n활성화된 페어 수: {len(symbol_list)}개")
    
    # 가격 정보 가져오기
    print("\n가격 정보 로드 중...")
    lastprices = exHL.fetch_tickers(symbol_list)
    
    # 효율적인 OI 수집을 위해 배치 처리
    print("\nOI 정보 수집 중 (배치 처리)...")
    
    # 각 배치에 포함할 심볼 수
    batch_size = 10
    
    # 배치 처리를 위한 설정
    oi_data_dict = {}
    total_batches = (len(symbol_list) + batch_size - 1) // batch_size
    
    for batch_index in range(total_batches):
        start_idx = batch_index * batch_size
        end_idx = min(start_idx + batch_size, len(symbol_list))
        batch_symbols = symbol_list[start_idx:end_idx]
        
        print(f"배치 처리 중: {batch_index + 1}/{total_batches}...")
        
        try:
            # 배치 단위로 OI 정보 가져오기
            batch_oi_data = exHL.fetch_open_interests(batch_symbols)
            time.sleep(1)  # API 제한 방지
            
            # 결과 처리
            for symbol, oi_data in batch_oi_data.items():
                if 'openInterestAmount' in oi_data:
                    # 코인명 추출
                    coin = symbol.split('/')[0]
                    if ':' in coin:
                        coin = coin.split(':')[0]
                        
                    # USD 가치 계산
                    if symbol in lastprices and 'last' in lastprices[symbol] and lastprices[symbol]['last']:
                        price = lastprices[symbol]['last']
                        oi_amount = oi_data.get('openInterestAmount', 0)
                        if oi_amount:  # None이 아닌 경우에만 계산
                            oi_value = oi_amount * price
                            oi_data_dict[coin] = int(oi_value)
        except Exception as e:
            print(f"배치 처리 오류 (건너뜀): {str(e)}")
    
    print(f"\nOI 정보 수집 완료: {len(oi_data_dict)}개 코인 처리됨")
    
    # k 접두사 처리
    k_prefix_coins = {}
    coins_to_remove = []
    
    # k 접두사를 가진 코인 찾기
    for coin in oi_data_dict.keys():
        if coin.startswith('k'):
            original_name = coin[1:]  # k 제거
            k_prefix_coins[coin] = original_name
            coins_to_remove.append(coin)
    
    # k 접두사 코인 처리
    for k_coin, original_name in k_prefix_coins.items():
        # OI 값 합산
        if original_name in oi_data_dict:
            # 원래 이름이 이미 있는 경우 OI 값 합산
            print(f"합산: {k_coin} -> {original_name}")
            oi_data_dict[original_name] += oi_data_dict[k_coin]
        else:
            # 원래 이름이 없는 경우 k 제거한 이름으로 항목 추가
            print(f"변환: {k_coin} -> {original_name}")
            oi_data_dict[original_name] = oi_data_dict[k_coin]
    
    # k 접두사 코인 제거
    for coin in coins_to_remove:
        del oi_data_dict[coin]
    
    # OI 내림차순 정렬
    sorted_oi_dict = dict(sorted(oi_data_dict.items(), key=lambda x: x[1], reverse=True))
    
    # 모든 OI 출력
    print("\nHyperLiquid 모든 페어의 OI:")
    for ticker, oi in sorted_oi_dict.items():
        print(f"{ticker}: ${oi:,}")
    
    # 전체 OI 합계
    total_oi = sum(sorted_oi_dict.values())
    print(f"\n전체 OI 합계: ${total_oi:,}")
    
    # 모듈 레벨 변수에 값 할당
    Tickerlist.clear()  # 기존 리스트 비우기
    Tickerlist.extend(list(sorted_oi_dict.keys()))  # 새 값으로 채우기
    
    # OI 딕셔너리 업데이트
    sorted_OI_Dict.clear()  # 기존 딕셔너리 비우기
    sorted_OI_Dict.update(sorted_oi_dict)  # 새 값으로 채우기
    
except Exception as e:
    error_message = f"HyperLiquid 데이터 수집 중 오류 발생: {str(e)}"
    print(error_message)
    SlackModule.Exchange_Listing_send_message_to_slack(error_message) 
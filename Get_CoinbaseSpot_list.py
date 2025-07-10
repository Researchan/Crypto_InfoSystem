import ccxt
import SlackModule
import re

try:
    # 코인베이스 거래소 인스턴스 생성 (API 키 없이)
    exCB = ccxt.coinbase()
    
    # 모든 심볼 가져오기
    all_symbols = exCB.load_markets().keys()
    
    # USD 페어만 필터링
    Tickerlist = []
    for symbol in all_symbols:
        if '/USD' in symbol:
            ticker = symbol.split('/')[0]
            Tickerlist.append(ticker)
    
    # 중복 제거
    Tickerlist = set(Tickerlist)
    Tickerlist = list(Tickerlist)
    
    # 초기 토큰 수 기록
    initial_token_count = len(Tickerlist)
    # print(f"초기 USD 페어 수: {initial_token_count}")
    
    # 제외할 토큰 목록
    tokens_to_remove = [
        'USDT', 'USDC', 'BUSD', 'DAI',  # 스테이블코인
        'WBTC', 'WETH', 'WAXL',  # 랩핑 토큰
        'CBETH', 'LSETH',  # 스테이킹 토큰
        'PYUSD', 'GUSD', 'EURC',  # 기타 스테이블코인
        'MSOL',  # 솔라나 스테이킹 토큰
        'BIT', 'PAX',  # 기타 제거 대상
        'KARRAT',  # 이름 변경 필요한 토큰??
        '00',  # 00 티커 제거
        'OCEAN',  # Ocean Protocol이 합병됨 (대체 토큰 없음)
        'COIN50',  # 인덱스 토큰
        'DAR',  # DAR이 D로 리브랜딩되었지만 코인베이스에 미상장
        'GST', # 쓰레기.
    ]
    
    # CDE로 시작하는 모든 토큰 제거
    cde_tokens = [token for token in Tickerlist if token.startswith('CDE')]
    tokens_to_remove.extend(cde_tokens)
    
    # 토큰 이름 변경 (1:1 매핑)
    token_mappings = {
        'ZETACHAIN': 'ZETA',  # ZETACHAIN을 ZETA로 변경
        'CORECHAIN': 'CORE',  # CORECHAIN을 CORE로 변경
        'RONIN': 'RON',       # RONIN을 RON으로 변경
        'WCFG': 'CFG',        # WCFG를 CFG로 변경
        'WAMPL': 'AMPL',      # WAMPL을 AMPL로 변경
        'RNDR': 'RENDER',     # RNDR이 RENDER로 리브랜딩됨
        'MATIC': 'POL',       # MATIC이 POL로 리브랜딩됨
        'MPL': 'SYRUP',       # MPL이 SYRUP으로 합병됨
        'LIT': 'HEI',          # LIT이 HEI로 리브랜딩됨
        'MANTLE': 'MNT'          # 티커 변경
    }
    
    # 제외된 토큰 출력
    # print("\n제외된 토큰 목록:")
    # for token in sorted(tokens_to_remove):
    #     if token in Tickerlist:
    #         print(f"- {token}")
    
    # 토큰 제거
    for token in tokens_to_remove:
        if token in Tickerlist:
            Tickerlist.remove(token)
    
    # 1000이 들어간 모든 티커 찾기
    thousand_tokens = [token for token in Tickerlist if '1000' in token]
    # print("\n1000이 들어간 토큰 목록:")
    # for token in sorted(thousand_tokens):
    #     print(f"- {token}")
    
    # 1000이 들어간 토큰들에 대한 매핑 추가
    for token in thousand_tokens:
        new_name = re.sub(r'1000', '', token)  # 1000 제거
        token_mappings[token] = new_name
    
    # 토큰 이름 변경 적용
    # print("\n토큰 이름 변경이 적용됨:")
    for old_name, new_name in token_mappings.items():
        if old_name in Tickerlist:
            # print(f"- {old_name} -> {new_name}")
            Tickerlist.remove(old_name)
            if new_name not in Tickerlist:
                Tickerlist.append(new_name)
    
    # 정렬
    Tickerlist.sort()
    
    # 결과 출력
    # print(f"\n총 {len(Tickerlist)}개의 USD 페어가 있습니다 (초기: {initial_token_count}):")
    # for ticker in Tickerlist:
    #     print(ticker)

except Exception as e:
    error_message = f"코인베이스 데이터 수집 중 오류 발생: {str(e)}"
    print(error_message)
    SlackModule.Exchange_Listing_send_message_to_slack(error_message) 
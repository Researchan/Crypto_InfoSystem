import ccxt
import time

print("Testing HyperLiquid OI functions:\n")

# 거래소 객체 생성
exchange = ccxt.hyperliquid({'options': {'defaultType': 'swap'}})

# 마켓 로드
print("마켓 데이터 로드 중...")
exchange.load_markets()
time.sleep(1)  # API 제한 방지를 위한 대기

symbol = 'BTC/USDC:USDC'

try:
    result = exchange.fetch_open_interest(symbol)
    print(f"\nfetch_open_interest 성공: {result}")
except Exception as e:
    print(f"\nfetch_open_interest 실패: {str(e)}")

time.sleep(1)

try:
    result = exchange.fetch_open_interests([symbol])
    print(f"\nfetch_open_interests 성공: {result}")
except Exception as e:
    print(f"\nfetch_open_interests 실패: {str(e)}")

time.sleep(1)

def safe_open_interest(exchange, symbol):
    try:
        result = exchange.fetch_open_interest(symbol)
        return {
            'symbol': symbol,
            'openInterest': result.get('openInterestAmount', 0)
        }
    except Exception as e:
        print(f"Error fetching open interest for {symbol}: {str(e)}")
        return {
            'symbol': symbol,
            'openInterest': 0
        }

time.sleep(1)

try:
    raw_data = exchange.fetch_open_interest(symbol, True)
    print(f"\nparse_open_interest 테스트용 원시 데이터: {raw_data}")
except Exception as e:
    print(f"\n원시 데이터 가져오기 실패: {str(e)}")

time.sleep(1)

# 여러 심볼 테스트
symbols = ['BTC/USDC:USDC', 'ETH/USDC:USDC', 'SOL/USDC:USDC']
try:
    result = exchange.fetch_open_interests(symbols)
    print(f"\n여러 심볼 fetch_open_interests 성공: {result}")
except Exception as e:
    print(f"\n여러 심볼 fetch_open_interests 실패: {str(e)}")

time.sleep(1)

# 모든 심볼 테스트
print("\n처음 10개 심볼 fetch_open_interests 테스트:")
# 실제 거래되는 주요 심볼 목록 정의
valid_symbols = ['BTC/USDC:USDC', 'ETH/USDC:USDC', 'SOL/USDC:USDC', 'AVAX/USDC:USDC', 'MATIC/USDC:USDC']
results = {}

for symbol in valid_symbols[:10]:  # 처음 10개 또는 가능한 만큼의 심볼 테스트
    try:
        oi_data = exchange.fetch_open_interest(symbol)
        results[symbol] = oi_data
        time.sleep(1)  # API 레이트 리밋 방지
    except Exception as e:
        print(f"Error for {symbol}: {str(e)}")

print(f"\n총 {len(results)} 개의 유효한 결과")
print("\n첫 3개 결과:")
for i, (symbol, data) in enumerate(list(results.items())[:3]):
    print(f"{symbol}: {data['openInterestAmount']} {symbol.split('/')[0]}") 
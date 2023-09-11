import requests

# 바이낸스 API 엔드포인트 URL
url = 'https://fapi.binance.com/futures/data/openInterestHist'

# 요청 파라미터 설정
params = {
    'symbol': 'BTCUSDT',  # 페어 심볼
    'period': '5m',
    'limit': 5  # 가져올 데이터 수 (예: 최근 5개)
}

try:
    # 요청 보내기
    response = requests.get(url, params=params)

    # 요청이 성공적으로 완료되었는지 확인
    if response.status_code == 200:
        print(response.status_code)
        data = response.json()
        # for item in data:
        #     print(f"Open Interest 히스토리 데이터: {item}")
        print(data)
    else:
        print(f"요청 실패. 상태 코드: {response.status_code, response.json()}")
        
except Exception as e:
    print(f"오류 발생: {str(e)}")
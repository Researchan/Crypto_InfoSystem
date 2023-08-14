import requests
import pandas as pd

# Coingecko API 주소
url = 'https://api.coingecko.com/api/v3/coins/markets'

# 엑셀 파일에서 ids 정보를 가져옴
df = pd.read_excel('output.xlsx')

# 엑셀 파일에 있는 id들을 ','로 구분하여 문자열로 만듦
ids = ",".join(df['CG_id'].tolist())

# API 호출에 사용할 파라미터
params = {
    'vs_currency': 'usd',
    'ids': ids,
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': False
}

# 모든 코인의 정보를 저장할 딕셔너리 생성
all_coins_data = {}

for _ in range(3):  # 3 페이지까지 조회
    try:
        response = requests.get(url, params=params)
        response_json = response.json()

        # API 호출 결과가 빈 리스트인 경우, 더 이상 정보가 없으므로 반복문 종료
        if not response_json:
            break

        # 모든 코인의 정보를 딕셔너리에 추가
        for coin_info in response_json:
            all_coins_data[coin_info['id']] = {
                'market_cap': coin_info['market_cap'],
                'FDV': coin_info['fully_diluted_valuation']
            }

        # 다음 페이지로 이동하기 위해 'page' 파라미터를 증가시킴
        params['page'] += 1
    except Exception as e:
        # API 호출이 실패한 경우 에러 메시지 출력
        print(response_json)
        print("Error: Failed to retrieve data", e)
        break

# 'all_coins_data' 딕셔너리에 해당 코인의 정보가 없는 경우에는 NaN을 기본값으로 설정
df['market_cap'] = df['CG_id'].map(lambda x: all_coins_data[x]['market_cap'] if x in all_coins_data else float('nan'))
df['FDV'] = df['CG_id'].map(lambda x: all_coins_data[x]['FDV'] if x in all_coins_data else float('nan'))

# 새로운 엑셀 파일로 저장
df.to_excel('output_with_data_CG.xlsx', index=False)
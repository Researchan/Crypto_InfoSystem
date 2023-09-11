import requests
import pandas as pd

# Coingecko API 주소
coingecko_url = 'https://api.coingecko.com/api/v3/coins/markets'

# CoinMarketCap API 주소
coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

# API 키 입력
coinmarketcap_api_key = '339f7745-0a39-4c98-924a-39f07902c361'

# 엑셀 파일에서 ids 정보를 가져옴
df = pd.read_excel('output.xlsx')

# 엑셀 파일에 있는 id들을 ','로 구분하여 문자열로 만듦
coingecko_ids = ",".join(df['CG_id'].tolist())

# Coingecko API 호출에 사용할 파라미터
coingecko_params = {
    'vs_currency': 'usd',
    'ids': coingecko_ids,
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': False
}

# 모든 코인의 정보를 저장할 딕셔너리 생성
coingecko_coins_data = {}

# Coingecko API 호출 및 데이터 처리
for _ in range(10):  # 10 페이지까지 조회
    try:
        response = requests.get(coingecko_url, params=coingecko_params)
        response_json = response.json()

        # API 호출 결과가 빈 리스트인 경우, 더 이상 정보가 없으므로 반복문 종료
        if not response_json:
            break

        # 모든 코인의 정보를 딕셔너리에 추가
        for coin_info in response_json:
            coingecko_coins_data[coin_info['id']] = {
                'market_cap': coin_info['market_cap'],
                'FDV': coin_info['fully_diluted_valuation']
            }

        # 다음 페이지로 이동하기 위해 'page' 파라미터를 증가시킴
        coingecko_params['page'] += 1
    except:
        # API 호출이 실패한 경우 에러 메시지 출력
        print("Error: Failed to retrieve Coingecko data")
        break

# CoinMarketCap API 호출에 사용할 파라미터
coinmarketcap_params = {
    'id': ",".join(df['CMC_id'].astype(int).astype(str)),  # 여기서 정수형으로 변환한 후 다시 문자열로 변환
}

# CoinMarketCap API 호출에 필요한 헤더
coinmarketcap_headers = {
    'X-CMC_PRO_API_KEY': coinmarketcap_api_key,
}

# CoinMarketCap API 호출 및 데이터 처리
try:
    response = requests.get(coinmarketcap_url, params=coinmarketcap_params, headers=coinmarketcap_headers)
    response_json = response.json()

    # API 호출 결과에 문제가 있는 경우 종료
    if 'data' not in response_json:
        print("Error: No CoinMarketCap data found.")
        exit()

    # 모든 코인의 정보를 딕셔너리에 추가
    coinmarketcap_coins_data = response_json['data']

    # 코인별로 데이터를 정리하여 저장할 리스트 생성
    coin_data_list = []

    # 코인별로 데이터를 정리하여 리스트에 추가
    for _, row in df.iterrows():
        cg_id = row['CG_id']
        cmc_id = row['CMC_id']

        cg_market_cap = coingecko_coins_data.get(cg_id, {}).get('market_cap', float('nan'))
        cg_fdv = coingecko_coins_data.get(cg_id, {}).get('FDV', float('nan'))

        cmc_market_cap = coinmarketcap_coins_data.get(str(cmc_id), {}).get('quote', {}).get('USD', {}).get('market_cap', float('nan'))
        cmc_fdv = coinmarketcap_coins_data.get(str(cmc_id), {}).get('quote', {}).get('USD', {}).get('fully_diluted_market_cap', float('nan'))

        coin_data_list.append([cg_id, cmc_id, cg_market_cap, cg_fdv, cmc_market_cap, cmc_fdv])

    # 데이터를 DataFrame으로 변환
    columns = ['CG_id', 'CMC_id', 'CG_MarketCap', 'CG_FDV', 'CMC_MarketCap', 'CMC_FDV']
    df_combined = pd.DataFrame(coin_data_list, columns=columns)

    # 새로운 엑셀 파일로 저장
    df_combined.to_excel('output_combined.xlsx', index=False)

    print("Data retrieval successful and saved to output_combined.xlsx!")

except Exception as e:
    print("Error: Failed to retrieve CoinMarketCap data -", e)
import requests
import pandas as pd

# CoinMarketCap API 주소
url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

# API 키 입력
api_key = '339f7745-0a39-4c98-924a-39f07902c361'

# 엑셀 파일에서 CMC_id 정보를 가져옴
df = pd.read_excel('output.xlsx')

# 엑셀 파일에 있는 CMC_id들을 ','로 구분하여 문자열로 만듦
ids = ",".join(df['CMC_id'].astype(int).astype(str))  # 여기서 정수형으로 변환한 후 다시 문자열로 변환
#ids = '8104,7278,6958,2010,2424,4030,8766,7232,2081,3783,1680,18876,7737,21794,5632,11841,4039,12885,10188,3794,7455,5805,6783,7064,5728,4679,1697,1831,6928,23121,2505,1839,23635,1,10903,5567,3814,7334,3978,4066,4948,4275,5692,3992,6538,4807,5444,9903,11374'

# API 호출에 사용할 파라미터
params = {
    'id': ids,
}

# API 호출에 필요한 헤더
headers = {
    'X-CMC_PRO_API_KEY': api_key,
}

# API 호출 및 데이터 처리
try:
    response = requests.get(url, params=params, headers=headers)
    response_json = response.json()

    # API 호출 결과에 문제가 있는 경우 종료
    if 'data' not in response_json:
        print("Error: No data found.")
        exit()

    # 모든 코인의 정보를 딕셔너리에 추가
    all_coins_data = response_json['data']
    

    # 데이터 출력
    for _, row in df.iterrows():
        cmc_id = str(row['CMC_id'])
        if cmc_id in all_coins_data:
            market_cap = all_coins_data[cmc_id]['quote']['USD']['market_cap']
            fdv = all_coins_data[cmc_id]['quote']['USD']['fully_diluted_market_cap']  # 여기서 수정
            print(f"CMC_id: {cmc_id}, Market Cap: {market_cap}, FDV: {fdv}")
        else:
            print(f"CMC_id: {cmc_id}, Data not found")

    print("Data retrieval successful!")

except Exception as e:
    print("Error: Failed to retrieve data -", e)

    # 'market_cap'과 'FDV' 정보를 데이터프레임에 추가
#     df['market_cap'] = df['CMC_id'].map(lambda x: all_coins_data[str(x)]['quote']['USD']['market_cap'] if str(x) in all_coins_data else float('nan'))
#     df['FDV'] = df['CMC_id'].map(lambda x: all_coins_data[str(x)]['quote']['USD']['fully_diluted_valuation'] if str(x) in all_coins_data else float('nan'))

#     # 새로운 엑셀 파일로 저장
#     df.to_excel('output_with_data3.xlsx', index=False)
#     print("Data retrieval and saving successful!")

# except Exception as e:
#     print("Error: Failed to retrieve data -", e)
# 
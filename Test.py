import requests

def get_open_interest(symbol):
    url = "https://fapi.binance.com/fapi/v1/openInterest"
    params = {'symbol': symbol}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code, response.text

# 예시 사용
symbol = "TOMOUSDT" 
open_interest_data = get_open_interest(symbol)
print(open_interest_data)
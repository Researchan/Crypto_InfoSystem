import requests
from requests.exceptions import HTTPError
import json
from urllib import request, parse
import ssl
import certifi



# 모든 BTC 코인 조회하기 
def Get_Bithumb_BTC_Tickers():
    req = request.Request('https://api.bithumb.com/public/ticker/ALL_BTC')
    res = request.urlopen(req)
    # print(str(res.status) + " | " + res.read().decode('utf-8'))

    resultString = res.read().decode('utf-8')
    result = json.loads(resultString)
    data = result["data"]
    keys_list = list(data)

    return(keys_list)
    
# 모든 KRW 코인 불러오기
def Get_Bithumb_KRW_Tickers():
    req = request.Request('https://api.bithumb.com/public/ticker/ALL_KRW')
    res = request.urlopen(req)
    # print(str(res.status) + " | " + res.read().decode('utf-8'))

    resultString = res.read().decode('utf-8')
    result = json.loads(resultString)
    data = result["data"]
    keys_list = list(data)

    return(keys_list)

def Get_Bithumb_All_Tickers():
    All_Tickers = Get_Bithumb_BTC_Tickers() + Get_Bithumb_KRW_Tickers()
    Temp = set(All_Tickers)
    All_Tickers = list(Temp)
    All_Tickers.sort()
    
    return(All_Tickers)

print(Get_Bithumb_All_Tickers())
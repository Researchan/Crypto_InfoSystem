import ccxt 
import time
from jandimodule import *
import unicodedata

exBNfuture = ccxt.binanceusdm()
exBNfutureTickersInfo = exBNfuture.fetchTickers() # 티커 딕셔너리 가져옴
exBNfutureTickers = exBNfutureTickersInfo.keys() # 티커 키만 받아오기 (이름만)
Tickers = []

for i in exBNfutureTickers:
    if '-' not in i and 'USDT' in i:
        Tickers.append(i[0:-5])
    
Tickers.remove('COCOS/USDT')
Tickers.remove('DEFI/USDT')
Tickers.remove('BLUEBIRD/USDT')
Tickers.remove('FOOTBALL/USDT')
Tickers.sort()


OI_Dict ={}
Change_24h ={}
Change_4h ={}
Change_1h ={}

while True:
    try:
        for i in Tickers:
            res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
                'limit':'289',
            })
            #현재 OI
            OI_Dict[str(i)] = round(res[288]['openInterestValue'])
            
            #24시간 증감율
            Change_24h[str(i)] = {'Change_Pct' : round((((res[288]['openInterestValue'] - res[0]['openInterestValue']) / res[0]['openInterestValue']) * 100)*100)/100,
                                'OpenInterestValue_t00' : round(res[288]['openInterestValue']),
                                'OpenInterestValue_t24' : round(res[0]['openInterestValue']),
                                'Change_Amt' : round(res[288]['openInterestValue'])-round(res[0]['openInterestValue'])
                                }

            print(Change_24h[i])
            
            #4시간 증감율
            Change_4h[str(i)] = {'Change_Pct' : round((((res[288]['openInterestValue'] - res[240]['openInterestValue']) / res[240]['openInterestValue']) * 100)*100)/100,
                                'OpenInterestValue_t00' : round(res[288]['openInterestValue']),
                                'OpenInterestValue_t04' : round(res[240]['openInterestValue']),
                                'Change_Amt' : round(res[288]['openInterestValue'])-round(res[240]['openInterestValue'])
                                }

            #1시간 증감율
            Change_1h[str(i)] = {'24hr_change%' : round((((res[288]['openInterestValue'] - res[276]['openInterestValue']) / res[276]['openInterestValue']) * 100)*100)/100,
                                'OpenInterestValue_t00' : round(res[288]['openInterestValue']),
                                'OpenInterestValue_t01' : round(res[276]['openInterestValue']),
                                'Change_Amount' : round(res[288]['openInterestValue'])-round(res[276]['openInterestValue'])
                                }
            
            # OI 내림차순, 오름차순
        Descend_OI = sorted(OI_Dict.items(), key=lambda x: x[1], reverse=True) 
        Ascend_OI = sorted(OI_Dict.items(), key=lambda x: x[1], reverse=False)
        
            # 24시간 변화율 내림차순, 오름차순
        Descend_24h = sorted(Change_24h.items(), key=lambda x: x[1]['24hr_change%'], reverse=True) 
        Ascend_24h = sorted(Change_24h.items(), key=lambda x: x[1]['24hr_change%'], reverse=False)
        
            # 4시간 변화율 내림차순, 오름차순
        Descend_4h = sorted(Change_4h.items(), key=lambda x: x[1], reverse=True) 
        Ascend_4h = sorted(Change_4h.items(), key=lambda x: x[1], reverse=False)
        
            # 1시간 변화율 내림차순, 오름차순
        Descend_1h = sorted(Change_1h.items(), key=lambda x: x[1], reverse=True) 
        Ascend_1h = sorted(Change_1h.items(), key=lambda x: x[1], reverse=False)
        
        Descend_24h_Message = ''
        for i in range (5):
            Descend_24h_Message += (str(Descend_24h[i])+'\n')
        print(Descend_24h_Message)
            
        Ascend_24h_Message = ''
        for i in range (5):
            Ascend_24h_Message += (str(Ascend_24h[i])+'\n')
        print(Ascend_24h_Message)
        
        # # OI 상위 10개 메세지 전송
        # Descend_OI_Message = ''
        # for i in range(10):
        #     Descend_OI_Message += (str(Descend_OI[i])+'\n')
        
        # # 줄바꿈 문자('\n')를 기준으로 메세지를 분리하고, 각 행을 가공
        # lines = Descend_OI_Message.strip().split('\n')
        # formatted_message = ''
        
        # for line in lines:
        #     pair, value = eval(line)  # 문자열을 튜플로 변환
        #     coin, currency = pair.split('/')
        #     value_str = '${:,.0f}'.format(value)  # 숫자를 USD 형식으로 포맷팅
        #     formatted_line = f'{coin}\n{value_str}\n\n'
        #     formatted_message += formatted_line
        
        # formatted_message = formatted_message.rstrip()
        # OI_Alert_send_message_to_jandi('***OI Volume Top10 List***\n\n' + formatted_message)
        
        
        # # OI 하위 10개 메세지 전송
        # Ascend_OI_Message = ''
        # for i in range(10):
        #     Ascend_OI_Message += (str(Ascend_OI[i])+'\n')
        
        # # 줄바꿈 문자('\n')를 기준으로 메세지를 분리하고, 각 행을 가공
        # lines = Ascend_OI_Message.strip().split('\n')
        # formatted_message = ''
        
        # for line in lines:
        #     pair, value = eval(line)  # 문자열을 튜플로 변환
        #     coin, currency = pair.split('/')
        #     value_str = '${:,.0f}'.format(value)  # 숫자를 USD 형식으로 포맷팅
        #     formatted_line = f'{coin}\n{value_str}\n\n'
        #     formatted_message += formatted_line
            
        # formatted_message = formatted_message.rstrip()
        # OI_Alert_send_message_to_jandi('***OI Volume Bottom10 List***\n\n' + formatted_message)
            
        
    except Exception as e:
            print(i, ':', str(e))
    
    time.sleep(600)
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
            
            # OI 내림차순, 오름차순
        Descend_OI = sorted(OI_Dict.items(), key=lambda x: x[1], reverse=True) 
        Ascend_OI = sorted(OI_Dict.items(), key=lambda x: x[1], reverse=False)
        
        # OI 상위 20개 메세지 전송
        Descend_OI_Message = ''
        for i in range(20):
            Descend_OI_Message += (str(Descend_OI[i])+'\n')
        
        lines = Descend_OI_Message.strip().split('\n') # 줄바꿈 문자('\n')를 기준으로 메세지를 분리하고, 각 행을 가공
        formatted_message = ''
        
        for line in lines:
            pair, value = eval(line)  # 문자열을 튜플로 변환
            coin, currency = pair.split('/')
            value_str = '${:,.0f}'.format(value)  # 숫자를 USD 형식으로 포맷팅
            formatted_line = f'{coin}\n{value_str}\n\n'
            formatted_message += formatted_line
        
        formatted_message = formatted_message.rstrip()
        OI_Alert_send_message_to_jandi('***OI Volume Top20 List***\n\n' + formatted_message)
        
        time.sleep(30)
        
        # OI 하위 20개 메세지 전송
        Ascend_OI_Message = ''
        for i in range(20):
            Ascend_OI_Message += (str(Ascend_OI[i])+'\n')
        
        lines = Ascend_OI_Message.strip().split('\n') # 줄바꿈 문자('\n')를 기준으로 메세지를 분리하고, 각 행을 가공
        formatted_message = ''
        
        for line in lines:
            pair, value = eval(line)  # 문자열을 튜플로 변환
            coin, currency = pair.split('/')
            value_str = '${:,.0f}'.format(value)  # 숫자를 USD 형식으로 포맷팅
            formatted_line = f'{coin}\n{value_str}\n\n'
            formatted_message += formatted_line
            
        formatted_message = formatted_message.rstrip()
        OI_Alert_send_message_to_jandi('***OI Volume Bottom20 List***\n\n' + formatted_message)
        
        time.sleep(30)
################################################ OI 24H ########################################################

        # OI 정보 수신
        for i in Tickers:
            res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
                'limit':'289',
            })
            OI_Dict[str(i)] = round(res[288]['openInterestValue']) # OI 정보 수신
        
        # OI 정보 가공 (24시간 증감율)
            Change_24h[str(i)] = {'Change_Pct' : round((((res[288]['openInterestValue'] - res[0]['openInterestValue']) / res[0]['openInterestValue']) * 100)*100)/100,
                                'OpenInterestValue_t00' : round(res[288]['openInterestValue']),
                                'OpenInterestValue_t24' : round(res[0]['openInterestValue']),
                                'Change_Amt' : round(res[288]['openInterestValue'])-round(res[0]['openInterestValue'])
                                }  
            
        # 24시간 변화율 내림차순, 오름차순 정렬
        Descend_24h = sorted(Change_24h.items(), key=lambda x: x[1]['Change_Pct'], reverse=True) 
        Ascend_24h = sorted(Change_24h.items(), key=lambda x: x[1]['Change_Pct'], reverse=False)
        
        # 24시간 OI 변화율 상위 5개 전송
        Descend_24h_Message = ''
        for i in range (5):
            pair, data = Descend_24h[i]
            message = f"**{pair}**\n"
            message += f"OI_Volume_00H : ${data['OpenInterestValue_t00']:,}\n"
            message += f"OI_Volume_24H : ${data['OpenInterestValue_t24']:,}\n"
            if data['Change_Amt'] < 0:
                message += f"24H_Change($) : -${-data['Change_Amt']:,}\n"
            else:
                message += f"24H_Change($) : ${data['Change_Amt']:,}\n"
            message += f"24H_Change(%) : {data['Change_Pct']:.2f}%\n\n"
            Descend_24h_Message += message
        OI_Alert_send_message_to_jandi("**24H OI Increase TOP5**\n\n" + Descend_24h_Message)
            
        # 24시간 OI 변화율 하위 5개 전송
        Ascend_24h_Message = ''
        for i in range (5):
            pair, data = Ascend_24h[i]
            message = f"**{pair}**\n"
            message += f"OI_Volume_00H : ${data['OpenInterestValue_t00']:,}\n"
            message += f"OI_Volume_24H : ${data['OpenInterestValue_t24']:,}\n"
            if data['Change_Amt'] < 0:
                message += f"24H_Change($) : -${-data['Change_Amt']:,}\n"
            else:
                message += f"24H_Change($) : ${data['Change_Amt']:,}\n"
            message += f"24H_Change(%) : {data['Change_Pct']:.2f}%\n\n"
            Ascend_24h_Message += message
        OI_Alert_send_message_to_jandi("**24H OI Decrease TOP5**\n\n" + Ascend_24h_Message)

        time.sleep(60)
################################################ OI 04H ########################################################

        # OI 정보 수신
        for i in Tickers:
            res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
                'limit':'289',
            })
            OI_Dict[str(i)] = round(res[288]['openInterestValue'])
        
        #OI 정보 가공(4시간 증감률)
            Change_4h[str(i)] = {'Change_Pct' : round((((res[288]['openInterestValue'] - res[240]['openInterestValue']) / res[240]['openInterestValue']) * 100)*100)/100,
                                'OpenInterestValue_t00' : round(res[288]['openInterestValue']),
                                'OpenInterestValue_t04' : round(res[240]['openInterestValue']),
                                'Change_Amt' : round(res[288]['openInterestValue'])-round(res[240]['openInterestValue'])
                                }
            
        # 4시간 변화율 내림차순, 오름차순 정렬
        Descend_04h = sorted(Change_4h.items(), key=lambda x: x[1]['Change_Pct'], reverse=True) 
        Ascend_04h = sorted(Change_4h.items(), key=lambda x: x[1]['Change_Pct'], reverse=False)
        
        # 변화율 상위 5개 메세지 전송
        Descend_04h_Message = ''
        for i in range (5):
            pair, data = Descend_04h[i]
            message = f"**{pair}**\n"
            message += f"OI_Volume_00H : ${data['OpenInterestValue_t00']:,}\n"
            message += f"OI_Volume_04H : ${data['OpenInterestValue_t04']:,}\n"
            if data['Change_Amt'] < 0:
                message += f"04H_Change($) : -${-data['Change_Amt']:,}\n"
            else:
                message += f"04H_Change($) : ${data['Change_Amt']:,}\n"
            message += f"04H_Change(%) : {data['Change_Pct']:.2f}%\n\n"
            Descend_04h_Message += message
        OI_Alert_send_message_to_jandi("**04H OI Increase TOP5**\n\n" + Descend_04h_Message)
        
        # 변화율 하위 5개 메세지 전송
        Ascend_04h_Message = ''
        for i in range (5):
            pair, data = Ascend_04h[i]
            message = f"**{pair}**\n"
            message += f"OI_Volume_00H : ${data['OpenInterestValue_t00']:,}\n"
            message += f"OI_Volume_04H : ${data['OpenInterestValue_t04']:,}\n"
            if data['Change_Amt'] < 0:
                message += f"04H_Change($) : -${-data['Change_Amt']:,}\n"
            else:
                message += f"04H_Change($) : ${data['Change_Amt']:,}\n"
            message += f"04H_Change(%) : {data['Change_Pct']:.2f}%\n\n"
            Ascend_04h_Message += message
        OI_Alert_send_message_to_jandi("**04H OI Decrease TOP5**\n\n" + Ascend_04h_Message)

        time.sleep(60)
################################################ OI 01H ########################################################

        #OI 정보 수신
        for i in Tickers:
            res = exBNfuture.fetch_open_interest_history(i, timeframe='5m', params={
                'limit':'289',
            })
            OI_Dict[str(i)] = round(res[288]['openInterestValue'])
            
        #OI 정보 가공 (1시간 증감율)
            Change_1h[str(i)] = {'Change_Pct' : round((((res[288]['openInterestValue'] - res[276]['openInterestValue']) / res[276]['openInterestValue']) * 100)*100)/100,
                                'OpenInterestValue_t00' : round(res[288]['openInterestValue']),
                                'OpenInterestValue_t01' : round(res[276]['openInterestValue']),
                                'Change_Amt' : round(res[288]['openInterestValue'])-round(res[276]['openInterestValue'])
                                }
        # 1시간 변화율 내림차순, 오름차순 정렬
        Descend_01h = sorted(Change_1h.items(), key=lambda x: x[1]['Change_Pct'], reverse=True) 
        Ascend_01h = sorted(Change_1h.items(), key=lambda x: x[1]['Change_Pct'], reverse=False)
        
        # 변화율 상위 5개 메세지 전송
        Descend_01h_Message = ''
        for i in range (5):
            pair, data = Descend_01h[i]
            message = f"**{pair}**\n"
            message += f"OI_Volume_00H : ${data['OpenInterestValue_t00']:,}\n"
            message += f"OI_Volume_01H : ${data['OpenInterestValue_t01']:,}\n"
            if data['Change_Amt'] < 0:
                message += f"01H_Change($) : -${-data['Change_Amt']:,}\n"
            else:
                message += f"01H_Change($) : ${data['Change_Amt']:,}\n"
            message += f"01H_Change(%) : {data['Change_Pct']:.2f}%\n\n"
            Descend_01h_Message += message
        OI_Alert_send_message_to_jandi("**01H OI Increase TOP5**\n\n" + Descend_01h_Message)
        
        # 변화율 하위 5개 메세지 전송
        Ascend_01h_Message = ''
        for i in range (5):
            pair, data = Ascend_01h[i]
            message = f"**{pair}**\n"
            message += f"OI_Volume_00H : ${data['OpenInterestValue_t00']:,}\n"
            message += f"OI_Volume_01H : ${data['OpenInterestValue_t01']:,}\n"
            if data['Change_Amt'] < 0:
                message += f"01H_Change($) : -${-data['Change_Amt']:,}\n"
            else:
                message += f"01H_Change($) : ${data['Change_Amt']:,}\n"
            message += f"01H_Change(%) : {data['Change_Pct']:.2f}%\n\n"
            Ascend_01h_Message += message
        OI_Alert_send_message_to_jandi("**01H OI Decrease TOP5**\n\n" + Ascend_01h_Message)
        
        time.sleep(60)
    except Exception as e:
            print(i, ':', str(e))
    
    time.sleep(3600)
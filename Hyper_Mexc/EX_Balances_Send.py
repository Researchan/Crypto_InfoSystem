import ccxt
from jandimodule import *
import requests
import time
from hyperliquid.info import Info
from hyperliquid.utils import constants
from datetime import datetime

#서버컴 IP
exMEXC = ccxt.mexc({
    'apiKey':'mx0vglOQxFEh4IpMQd',
    'secret':'9726f9108d4b4d859e467fdce3ca4e2a',
    'options': {
        'defaultType': 'swap',
    },
})

# #사무실컴 IP
# exMEXC = ccxt.mexc({
#     'apiKey':'mx0vgly0HQunGbvp36',
#     'secret':'8d0711dd9bec4b70927ed11e144f5329',
#     'options': {
#         'defaultType': 'swap',
#     },
# })

while True:
    try:
        positions = exMEXC.fetch_positions()
        positions_info = {}
        usd_position_size_sum = 0

        tp_rates = [0.20, 0.24, 0.28, 0.32, 0.35]
        sl_rates = [-0.13, -0.15, -0.17, -0.19, -0.21, -0.23, -0.25, -0.27, -0.29, -0.31]

        for position in positions:
            symbol = position['symbol']
            contracts = position['contracts']
            contract_size = position['contractSize']
            size = contracts * contract_size
            
            ticker = exMEXC.fetch_ticker(symbol)

            price = float(ticker['info']['indexPrice'])
            
            # 소수점 자릿수 파악 
            decimal_places = len(str(price).split('.')[1]) if '.' in str(price) else 0

            # TP와 SL 계산
            tp_values = [round(price * (1 + rate), decimal_places-1) for rate in tp_rates]
            sl_values = [round(price * (1 + rate), decimal_places-1) for rate in sl_rates]
            
            
            positions_info[symbol] = {
                'size': size,
                'price': price,
                'TP1': tp_values[0],
                'TP2': tp_values[1],
                'TP3': tp_values[2],
                'TP4': tp_values[3],
                'TP5': tp_values[4],
                'SL1': sl_values[0],
                'SL2': sl_values[1],
                'SL3': sl_values[2],
                'SL4': sl_values[3],
                'SL5': sl_values[4],
                'SL6': sl_values[5],
                'SL7': sl_values[6],
                'SL8': sl_values[7],
                'SL9': sl_values[8],
                'SL10': sl_values[9]
            }
            # 포지션 사이즈 계산
            usd_position_size = size * price
            usd_position_size_sum += usd_position_size

        # 총 포지션 사이즈 도출
        usd_position_size_sum = round(usd_position_size_sum)
            
        # MEXC 잔고계산 및 도출
        res = exMEXC.fetch_balance()
        reslist = res['info']['data']
        for i in reslist:
            if i['currency'] == 'USDT':
                USDT_equity = round(float(i['equity']))


        # 총 레버리지 비율 계산

        leverage_multiple = round(usd_position_size_sum / USDT_equity, 2)

        #하리 계산
        user_address = '0x698DFc89aF0536ecAf73b2616dB6efFCa262fBB5'
        info = Info(constants.MAINNET_API_URL, skip_ws=True)
        user_state = info.user_state(user_address)
        account_equity = user_state['marginSummary']['accountValue']
        account_equity = float(account_equity)
        account_equity = round(account_equity)

        # 모두 전송
        send_message_to_jandi_Main('포지션 사이즈 : $' + str(usd_position_size_sum) +'\n' +
                                    'MEXC 잔고 : ' + str(USDT_equity) + ' USDT\n' +
                                    'MEXC 배율 : x'+ str(leverage_multiple) + '\n' +
                                    'HLQD 잔고 : ' + str(account_equity) + ' USDC\n' +
                                    'HLQD 배율 : x'+ str(round(usd_position_size_sum/account_equity,2))
                                    )
    
        time.sleep(300)
    except Exception as e:
        send_message_to_jandi_Main('하리멕시 잔고송신 파일 오류')
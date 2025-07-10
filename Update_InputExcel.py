import SlackModule
import traceback

import Get_BinanceFuture_list
import Get_Bithumb_list
import Get_BybitFuture_list
import Get_Upbit_BTC_list
import Get_Upbit_KRW_list
import Get_BinanceSpot_list
import Get_OkxFuture_list
import Get_HL_list
import Get_CoinbaseSpot_list
# import Get_BinanceFuture_OI
# import Get_BybitFuture_OI

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment

try:
    Upbit_KRW_list = Get_Upbit_KRW_list.Tickerlist
    Upbit_BTC_list = Get_Upbit_BTC_list.Tickerlist
    Bithumb_list = Get_Bithumb_list.Tickerlist
    Coinbase_Spot_list = Get_CoinbaseSpot_list.Tickerlist
    Binance_Spot_list = Get_BinanceSpot_list.Tickerlist
    Binance_Future_list = Get_BinanceFuture_list.Tickerlist
    Bybit_Future_list = Get_BybitFuture_list.Tickerlist
    Okx_Future_list = Get_OkxFuture_list.Tickerlist
    HL_Future_list = Get_HL_list.Tickerlist

    Binance_OI = Get_BinanceFuture_list.sorted_OI_Dict
    Bybit_OI = Get_BybitFuture_list.sorted_OI_Dict
    HL_OI = Get_HL_list.sorted_OI_Dict

    # 각 거래소 상장리스트 합산하여 전체 리스트 생성 및 정렬
    Coin_list = Upbit_KRW_list + Upbit_BTC_list + Bithumb_list + Coinbase_Spot_list + Binance_Spot_list + Binance_Future_list + Bybit_Future_list + Okx_Future_list + HL_Future_list
    Coin_list = set(Coin_list)
    Coin_list = list(Coin_list)
    Coin_list.sort()

    # 전체 정보를 담을 딕셔너리 생성
    Coin_Infos = {}

    for i in Coin_list:
        Coin_Infos[i] = {
            'Upbit_KRW':None,
            'Upbit_BTC':None,
            'Bithumb':None,
            'Coinbase_Spot':None,
            'Binance_Spot':None,
            'Binance_Future':None,
            'Bybit_Future':None,
            'Okx_Future':None,
            'HL_Future':None,
            'Binance_OI':None,
            'Bybit_OI':None,
            'HL_OI':None,
            'CG_id':None,
            'CMC_id':None
        }
        
        if i in Upbit_KRW_list:
            Coin_Infos[i]['Upbit_KRW'] = 'O'
        elif i not in Upbit_KRW_list:
            Coin_Infos[i]['Upbit_KRW'] = 'X'
            
        if i in Upbit_BTC_list:
            Coin_Infos[i]['Upbit_BTC'] = 'O'
        elif i not in Upbit_BTC_list:
            Coin_Infos[i]['Upbit_BTC'] = 'X'
            
        if i in Bithumb_list:
            Coin_Infos[i]['Bithumb'] = 'O'    
        elif i not in Bithumb_list:
            Coin_Infos[i]['Bithumb'] = 'X'
            
        if i in Coinbase_Spot_list:
            Coin_Infos[i]['Coinbase_Spot'] = 'O'
        elif i not in Coinbase_Spot_list:
            Coin_Infos[i]['Coinbase_Spot'] = 'X'
            
        if i in Binance_Spot_list:
            Coin_Infos[i]['Binance_Spot'] = 'O'
        elif i not in Binance_Spot_list:
            Coin_Infos[i]['Binance_Spot'] = 'X'
            
        if i in Binance_Future_list:
            Coin_Infos[i]['Binance_Future'] = 'O'
        elif i not in Binance_Future_list:
            Coin_Infos[i]['Binance_Future'] = 'X'
            
        if i in Bybit_Future_list:
            Coin_Infos[i]['Bybit_Future'] = 'O'
        elif i not in Bybit_Future_list:
            Coin_Infos[i]['Bybit_Future'] = 'X'

        if i in Okx_Future_list:
            Coin_Infos[i]['Okx_Future'] = 'O'
        elif i not in Okx_Future_list:
            Coin_Infos[i]['Okx_Future'] = 'X'
            
        if i in HL_Future_list:
            Coin_Infos[i]['HL_Future'] = 'O'
        elif i not in HL_Future_list:
            Coin_Infos[i]['HL_Future'] = 'X'
            
        if i in Binance_OI:
            Coin_Infos[i]['Binance_OI'] = Binance_OI[i]
            
        if i in Bybit_OI:
            Coin_Infos[i]['Bybit_OI'] = Bybit_OI[i]
            
        if i in HL_OI:
            Coin_Infos[i]['HL_OI'] = HL_OI[i]

    # 기존 엑셀 파일 불러오기 + Read로 열기
    Input_excel_file = 'ListingDatas.xlsx'
    df_excel = pd.read_excel(Input_excel_file)

    # 엑셀시트의 각 데이터 프레임을 반복해서 검색
    for _, row in df_excel.iterrows():
        ticker = row['Ticker'] # 엑셀파일에서, 행이름이 'Ticker'인 열의 데이터를 1행씩 가져와서 ticker변수에 할당
        # print(ticker)
        Coin_Infos[ticker]['CG_id'] = row['CG_id'] # 불러온 Ticker를 가지고 Coin_Infos Dictionary에서 검색해서, 있으면 해당 키의 CG_id 필드에 CG_id필드 정보 추가.
        # print(Coin_Infos[ticker]['CG_id'])
        Coin_Infos[ticker]['CMC_id'] = row['CMC_id'] # 같은 방식으로 CMC_id도 추가
        
    # 새로운 데이터프레임 생성
    new_data = []

    # 엑셀에 넣을 데이터 재할당.
    # 여기서의 ticker 변수는, Dict 자료의 key값을 의미함. 즉 위의 ticker와 헷갈리지 말기. 위의 for문안의 ticker는 소멸된다.
    for ticker, info in sorted(Coin_Infos.items()):
        new_row = {'Ticker': ticker, 'CG_id': info['CG_id'], 'CMC_id':info['CMC_id'],
                'Upbit_KRW': info['Upbit_KRW'], 'Upbit_BTC': info['Upbit_BTC'], 'Bithumb': info['Bithumb'], 'Coinbase_Spot': info['Coinbase_Spot'], 'Binance_Spot': info['Binance_Spot'], 
                'Binance_Future': info['Binance_Future'], 'Bybit_Future': info['Bybit_Future'], 'Okx_Future': info['Okx_Future'], 'HL_Future': info['HL_Future'],
                'Binance_OI': info['Binance_OI'], 'Bybit_OI': info['Bybit_OI'], 'HL_OI': info['HL_OI']}
        new_data.append(new_row)

    # 새로운 데이터를 기존 엑셀 파일에 추가. pandas사용.
    with pd.ExcelWriter(Input_excel_file, mode='a', engine='openpyxl',  if_sheet_exists='replace') as writer:
        existing_df = pd.DataFrame(new_data)
        existing_df.to_excel(writer, index=False, sheet_name='Sheet1')

    # 엑셀 규격 수정을 위해서 openpyxl로 열기.
    workbook = load_workbook(filename=Input_excel_file)

    # 원하는 시트 선택
    worksheet = workbook['Sheet1']

    # 열 넓이 설정
    worksheet.column_dimensions['A'].width = 15
    worksheet.column_dimensions['B'].width = 30
    worksheet.column_dimensions['C'].width = 10
    worksheet.column_dimensions['D'].width = 15
    worksheet.column_dimensions['E'].width = 15
    worksheet.column_dimensions['F'].width = 15
    worksheet.column_dimensions['G'].width = 15
    worksheet.column_dimensions['H'].width = 15
    worksheet.column_dimensions['I'].width = 15
    worksheet.column_dimensions['J'].width = 15
    worksheet.column_dimensions['K'].width = 15
    worksheet.column_dimensions['L'].width = 15
    worksheet.column_dimensions['M'].width = 15
    worksheet.column_dimensions['N'].width = 15
    worksheet.column_dimensions['O'].width = 15

    # A열부터 O열까지 가운데 정렬
    for column_letter in 'ABCDEFGHIJKLMNO':
        for cell in worksheet[column_letter]:
            cell.alignment = Alignment(horizontal='center', vertical='center')


            
    # 변경 내용 저장
    workbook.save(Input_excel_file)

    print(f"Data has been updated and saved to {Input_excel_file}.")

except Exception as e:
    print(e)
    print(traceback.format_exc())
    # if e == 'nan':
    #     pass
    SlackModule.Exchange_Listing_send_message_to_slack(str(e))
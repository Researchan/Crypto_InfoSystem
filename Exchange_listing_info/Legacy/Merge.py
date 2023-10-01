import Get_BinanceFuture_list
import Get_Bithumb_list
import Get_BybitFuture_list
import Get_Upbit_BTC_list
import Get_Upbit_KRW_list
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Alignment

Upbit_BTC_list = Get_Upbit_BTC_list.Tickerlist
Upbit_KRW_list = Get_Upbit_KRW_list.Tickerlist
Binance_Future_list = Get_BinanceFuture_list.Tickerlist
Bybit_Future_list = Get_BybitFuture_list.Tickerlist
Bithumb_list = Get_Bithumb_list.Tickerlist

# 각 거래소 상장리스트 합산하여 전체 리스트 생성 및 정렬
Coin_list = Upbit_KRW_list + Upbit_BTC_list + Binance_Future_list + Bybit_Future_list + Bithumb_list
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
        'Binance_Future':None,
        'Bybit_Future':None,
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
        
    if i in Binance_Future_list:
        Coin_Infos[i]['Binance_Future'] = 'O'
    elif i not in Binance_Future_list:
        Coin_Infos[i]['Binance_Future'] = 'X'
        
    if i in Bybit_Future_list:
        Coin_Infos[i]['Bybit_Future'] = 'O'
    elif i not in Bybit_Future_list:
        Coin_Infos[i]['Bybit_Future'] = 'X'
        
    if i in Bithumb_list:
        Coin_Infos[i]['Bithumb'] = 'O'    
    elif i not in Bithumb_list:
        Coin_Infos[i]['Bithumb'] = 'X'

# 기존 엑셀 파일 불러오기 + Read로 열기
Input_excel_file = 'ListingDatas_Test.xlsx'
df_excel = pd.read_excel(Input_excel_file)

# 각 데이터 프레임을 반복해서 검색, 엑셀데이터와 거래소상장데이터의 Ticker가 일치하는 경우 엑셀에 있던 id정보를 거래소 상장정보 딕셔너리에 정보추가.
for _, row in df_excel.iterrows():
    ticker = row['Ticker']
    Coin_Infos[ticker]['CG_id'] = row['CG_id']
    Coin_Infos[ticker]['CMC_id'] = row['CMC_id']
    
# 새로운 데이터프레임 생성
new_data = []

# 엑셀에 넣을 데이터 재할당.
for ticker, info in sorted(Coin_Infos.items()):
    new_row = {'Ticker': ticker, 'CG_id': info['CG_id'], 'CMC_id':info['CMC_id'], 'Upbit_KRW': info['Upbit_KRW'], 'Upbit_BTC': info['Upbit_BTC'], 'Bithumb': info['Bithumb'], 'Binance_Future': info['Binance_Future'], 'Bybit_Future': info['Bybit_Future']}
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

# A열부터 H열까지 가운데 정렬
for column_letter in 'ABCDEFGH':
    for cell in worksheet[column_letter]:
        cell.alignment = Alignment(horizontal='center', vertical='center')


        
# 변경 내용 저장
workbook.save(Input_excel_file)

print(f"Data has been updated and saved to {Input_excel_file}.")
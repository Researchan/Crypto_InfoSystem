import requests
import pandas as pd

input_file_name = 'Bithumb_Input.xlsx'
output_xlsx_name = 'Bithumb_Infos.xlsx'
output_html_name = 'Bithumb_Infos.html'

coingecko_url = 'https://api.coingecko.com/api/v3/coins/markets'
coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
coinmarketcap_api_key = '339f7745-0a39-4c98-924a-39f07902c361'

# 엑셀 파일에서 ids 정보를 가져옴
df = pd.read_excel(input_file_name)

# 엑셀 파일에 있는 id들을 ','로 구분하여 문자열로 만듦
# coingecko_ids = ",".join(df['CG_id'].tolist())
coingecko_ids = ",".join(df['CG_id'].fillna('').astype(str).tolist())

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
for _ in range(3):  # 3 페이지까지 조회
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
    except Exception as e:
        # API 호출이 실패한 경우 에러 메시지 출력
        print(response_json)
        print("Error: Failed to retrieve Coingecko data", e)
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
    # BithumbTicker를 사용하도록 업데이트
    for _, row in df.iterrows():
        cg_id = row['CG_id']
        cmc_id = row['CMC_id']
        bithumb_ticker = row['BithumbTicker']  # BithumbTicker 데이터 추가
        binance_future_listing = row['Binance_Future_listing']
        KRW_Listing = row['KRW_Listing']

        cg_market_cap = coingecko_coins_data.get(cg_id, {}).get('market_cap', float('nan'))
        cg_fdv = coingecko_coins_data.get(cg_id, {}).get('FDV', float('nan'))

        cmc_market_cap = coinmarketcap_coins_data.get(str(cmc_id), {}).get('quote', {}).get('USD', {}).get('market_cap', float('nan'))
        cmc_fdv = coinmarketcap_coins_data.get(str(cmc_id), {}).get('quote', {}).get('USD', {}).get('fully_diluted_market_cap', float('nan'))

        # 리스트에 추가 시 Binance_Future_listing과 KRW_Listing도 포함
        coin_data_list.append([bithumb_ticker, cg_id, cmc_id, cg_market_cap, cg_fdv, cmc_market_cap, cmc_fdv, binance_future_listing, KRW_Listing])

    # 데이터를 DataFrame으로 변환
    columns = ['BithumbTicker', 'CG_id', 'CMC_id', 'CG_MarketCap', 'CG_FDV', 'CMC_MarketCap', 'CMC_FDV', 'Binance_Future_listing', 'KRW_Listing']
    df_combined = pd.DataFrame(coin_data_list, columns=columns)

    # 새로운 엑셀 파일로 저장
    with pd.ExcelWriter(output_xlsx_name, engine='xlsxwriter') as writer:
        df_combined.to_excel(writer, index=False, sheet_name='Sheet1')

        # 엑셀 파일의 WorkSheet 객체 가져오기
        worksheet = writer.sheets['Sheet1']

        # A열의 넓이를 14로 설정
        worksheet.set_column('A:A', 14)

        # B열과 C열의 넓이를 최대한 줄여주기
        worksheet.set_column('B:C', None, None, {'hidden': True})

        # D, E, F, G열의 넓이를 15로 설정하고 통화 형식도 적용
        money_format = writer.book.add_format({'num_format': '$#,##0'})
        worksheet.set_column('D:G', 15, money_format)

    print(f"Data retrieval successful and saved to {output_xlsx_name}!")

    # 엑셀 데이터 읽어오기
    df = pd.read_excel(output_xlsx_name)
    df = df.drop(columns=['CG_id', 'CMC_id'])  # CG_id와 CMC_id 열을 제거
    
    # 결측값 처리
    df.fillna(0, inplace=True)  

    # pandas DataFrame을 HTML로 변환하기 전에 적용할 통화 형식
    df['CG_MarketCap'] = df['CG_MarketCap'].apply(lambda x: f"${int(x):,}")
    df['CG_FDV'] = df['CG_FDV'].apply(lambda x: f"${int(x):,}")
    df['CMC_MarketCap'] = df['CMC_MarketCap'].apply(lambda x: f"${int(x):,}")
    df['CMC_FDV'] = df['CMC_FDV'].apply(lambda x: f"${int(x):,}")

    df = df.reindex(columns=['BithumbTicker', 'Binance_Future_listing', 'KRW_Listing', 'CG_MarketCap', 'CMC_MarketCap', 'CG_FDV', 'CMC_FDV'])
    df.rename(columns={
        'Binance_Future_listing': '바낸 선물',
        'KRW_Listing': '원화',
        'CG_MarketCap': '유통 시가총액 (CG)',
        'CMC_MarketCap': '유통 시가총액 (CMC)',
        'CG_FDV': '총 시가총액 (CG)',
        'CMC_FDV': '총 시가총액(CMC)'
    }, inplace=True)
    
    # 행 번호를 별도의 열로 만들기
    df.reset_index(inplace=True)
    df.rename(columns={'index': ''}, inplace=True)

    # HTML 코드로 변환
    html = df.to_html(classes='dataframe', index=False)  # index=False 추가

    # HTML 파일로 저장
    with open(output_html_name, 'w', encoding='utf-8') as f:
        f.write('''
        <!DOCTYPE html>
        <html>
        <head>
        <title>Bithumb_listing_Info</title>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                }}
                .dataframe {{
                    width: 60%;
                    height: 80%;
                }}
                .dataTables_wrapper {{
                    width: 90%;
                    margin: auto;
                }}
                .custom-link {{
                    text-align:center;
                    padding-top: 10px;
                }}
                h1 {{
                    color: blue;
                    font-size: 24px;
                    text-align:center;
                }}
            </style>
            <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.css">
            <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
            <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.js"></script>
        </head>
        <body>
        <h1>Researchan's Bithumb listing Info Page</h1>
        <div class="custom-link">
            <a href="https://researchan.github.io/Crypto_InfoSystem/BinanceFuture_Infos.html">BinanceFuture_Infos</a>
            <a href="https://researchan.github.io/Crypto_InfoSystem/Upbit_Infos.html">Upbit_Infos</a>
        </div>
        <div class="dataTables_wrapper">
        {table}
        </div>
        <script>
        $(document).ready( function () {{
            var t = $('.dataframe').DataTable({{
                initComplete: function () {{
                    // 3열에 드롭다운 메뉴 추가
                    this.api().columns(2).every( function () {{
                        var column = this;
                        var select = $(
                        '<select><option value="">전체</option></select>'
                        )
                            .appendTo( $(column.header()) )
                            .on( 'change', function () {{
                                var val = $.fn.dataTable.util.escapeRegex(
                                    $(this).val()
                                );

                                column
                                    .search( val ? '^'+val+'$' : '', true, false )
                                    .draw();
                            }} );

                        column.data().unique().sort().each( function ( d, j ) {{
                            select.append( '<option value="'+d+'">'+d+'</option>' )
                        }} );
                    }} );

                    // 4열에 드롭다운 메뉴 추가
                    this.api().columns(3).every( function () {{
                        var column = this;
                        var select = $(
                        '<select><option value="">전체</option></select>'
                        )
                            .appendTo( $(column.header()) )
                            .on( 'change', function () {{
                                var val = $.fn.dataTable.util.escapeRegex(
                                    $(this).val()
                                );

                                column
                                    .search( val ? '^'+val+'$' : '', true, false )
                                    .draw();
                            }} );

                        column.data().unique().sort().each( function ( d, j ) {{
                            select.append( '<option value="'+d+'">'+d+'</option>' )
                        }} );
                    }} );
                }},
                "searching": true,
                "paging": false,
                "info": false,
                "lengthChange": false,
                "scrollY": '80vh',
                "scrollX": true,
                "scrollCollapse": true,
                "fixedHeader": true,
                "autoWidth": false,
                "order": [[ 1, "asc" ]],  // 2nd column as the initial sorting column
                "columnDefs": [ {{
                    "searchable": false,
                    "orderable": false,
                    "targets": 0
                }} ]
            }});

            // This will add numbers on the leftmost column
            t.on( 'order.dt search.dt', function () {{
                t.column(0, {{search:'applied', order:'applied'}}).nodes().each( function (cell, i) {{
                    cell.innerHTML = i+1;
                }});
            }}).draw();

        }});
        </script>
        </body>
        </html>
        '''.format(table=html))

    print(f"Data retrieval successful and saved to {output_html_name}!")
    
except Exception as e:
    print("Error :", e)
import requests
import pandas as pd
import jandimodule
import time  # time 모듈 추가

input_file_name = 'ListingDatas.xlsx'
output_xlsx_name = 'Dataoutput.xlsx'
output_html_name = 'ListingDatas.html'

coingecko_url = 'https://api.coingecko.com/api/v3/coins/markets'
coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
# coinmarketcap_api_key = '339f7745-0a39-4c98-924a-39f07902c361' #내꺼
coinmarketcap_api_key = 'a8c9a257-d8ad-43d4-84a8-a5a75d9a6ee4' #순호님

# 엑셀 파일에서 ids 정보를 가져옴
df = pd.read_excel(input_file_name)

# 엑셀 파일에 있는 id들을 ','로 구분하여 문자열로 만듦
#coingecko_ids = ",".join(df['CG_id'].tolist())
coingecko_ids = ",".join(df['CG_id'].fillna('').astype(str).tolist()) # CG_id가 없는 필드때문에 이렇게 사용해야함

id_list = coingecko_ids.split(',')

id_list1 = id_list[:500]
id_list2 = id_list[500:]

ids1_str = ",".join(id_list1)  # 최대 500개
ids2_str = ",".join(id_list2)  # 500개 이후 나머지

# Coingecko API 호출에 사용할 파라미터
coingecko1_params = {
    'vs_currency': 'usd',
    'ids': ids1_str,
    'order': 'market_cap_desc',
    'per_page': 200,
    'page': 1,
    'sparkline': False
}

coingecko2_params = {
    'vs_currency': 'usd',
    'ids': ids2_str,
    'order': 'market_cap_desc',
    'per_page': 200,
    'page': 1,
    'sparkline': False
}

# 모든 코인의 정보를 저장할 딕셔너리 생성
coingecko_coins_data = {}

# Coingecko API 호출 및 데이터 처리1
for _ in range(3):  # 3페이지까지 조회
    try:
        response = requests.get(coingecko_url, params=coingecko1_params)
        # print(response)
        # print(response.status_code)
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
        coingecko1_params['page'] += 1
        
        # API 호출 간 30초 대기 (기존 5초에서 변경)
        print("다음 API 호출 전 30초 대기 중...")
        time.sleep(30)
        
    except Exception as e:
        # API 호출이 실패한 경우 에러 메시지 출력
        print(response_json)
        print("Error: Failed to retrieve Coingecko data", e)
        jandimodule.Exchange_Listing_send_message_to_jandi(str(e))
        break

# 첫 번째 그룹과 두 번째 그룹 사이에 추가 대기 시간 (30초로 증가)
print("두 번째 API 호출 그룹 전 30초 대기 중...")
time.sleep(30)

# Coingecko API 호출 및 데이터 처리2
for _ in range(3):  # 3페이지까지 조회
    try:
        response = requests.get(coingecko_url, params=coingecko2_params)
        # print(response)
        # print(response.status_code)
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
        coingecko2_params['page'] += 1
        
        # API 호출 간 30초 대기 (기존 5초에서 변경)
        print("다음 API 호출 전 30초 대기 중...")
        time.sleep(30)
        
    except Exception as e:
        # API 호출이 실패한 경우 에러 메시지 출력
        print(response_json)
        print("Error: Failed to retrieve Coingecko data", e)
        jandimodule.Exchange_Listing_send_message_to_jandi(str(e))
        break

# 코인게코 API 호출 완료 후 코인마켓캡 API 호출 전 추가 대기 시간 (3초)
time.sleep(3)

try:
    # CoinMarketCap API 호출에 사용할 파라미터
    coinmarketcap_params = {
        'id': ",".join(df['CMC_id'].astype(int).astype(str)),  # 여기서 정수형으로 변환한 후 다시 문자열로 변환
    }

    # CoinMarketCap API 호출에 필요한 헤더
    coinmarketcap_headers = {
        'X-CMC_PRO_API_KEY': coinmarketcap_api_key,
    }

    # CoinMarketCap API 호출 및 데이터 처리

    response = requests.get(coinmarketcap_url, params=coinmarketcap_params, headers=coinmarketcap_headers)
    response_json = response.json()

    # 모든 코인의 정보를 딕셔너리에 추가
    coinmarketcap_coins_data = response_json['data']

    # 코인별로 데이터를 정리하여 저장할 리스트 생성
    coin_data_list = []

    # 코인별로 데이터를 정리하여 리스트에 추가
    # Input Data를 열별로 받아서, 리스트에 저장.
    for _, row in df.iterrows():
        cg_id = row['CG_id']
        cmc_id = row['CMC_id']
        Ticker = row['Ticker']
        Upbit_KRW = row['Upbit_KRW'] 
        Upbit_BTC = row['Upbit_BTC']
        Bithumb = row['Bithumb']
        Coinbase_Spot = row['Coinbase_Spot']
        Binance_Spot = row['Binance_Spot']
        Binance_Future = row['Binance_Future']
        Bybit_Future = row['Bybit_Future']
        Okx_Future = row['Okx_Future']
        HL_Future = row['HL_Future']
        Binance_OI = row['Binance_OI']
        Bybit_OI = row['Bybit_OI']
        HL_OI = row['HL_OI']  # 하이퍼리퀴드 OI 추가

        cg_market_cap = coingecko_coins_data.get(cg_id, {}).get('market_cap', float('nan'))
        cg_fdv = coingecko_coins_data.get(cg_id, {}).get('FDV', float('nan'))

        cmc_market_cap = coinmarketcap_coins_data.get(str(cmc_id), {}).get('quote', {}).get('USD', {}).get('market_cap', float('nan'))
        cmc_fdv = coinmarketcap_coins_data.get(str(cmc_id), {}).get('quote', {}).get('USD', {}).get('fully_diluted_market_cap', float('nan'))

        # 받아온 데이터 리스트에 포함 (리스트 안에 리스트 구조)
        coin_data_list.append([Ticker, cg_id, cmc_id, cg_market_cap, cg_fdv, cmc_market_cap, cmc_fdv, 
                                Binance_OI, Bybit_OI, HL_OI,  # HL_OI 추가
                                Upbit_KRW, Upbit_BTC, Bithumb, Coinbase_Spot,
                                Binance_Spot, Binance_Future, Bybit_Future, Okx_Future, HL_Future
                               ])

    # 데이터를 DataFrame으로 변환. 이는 각 열 이름
    columns = ['Ticker', 'CG_id', 'CMC_id', 'CG_MarketCap', 'CG_FDV', 'CMC_MarketCap', 'CMC_FDV',
                'Binance_OI', 'Bybit_OI', 'HL_OI',  # HL_OI 추가
                'Upbit_KRW', 'Upbit_BTC', 'Bithumb', 'Coinbase_Spot',
                'Binance_Spot', 'Binance_Future', 'Bybit_Future', 'Okx_Future', 'HL_Future'
               ]
    
    #위에 coin_data_list와 columns에서 지정한 열 합쳐서 총 자료 생성. 순서 일치해야함
    df_combined = pd.DataFrame(coin_data_list, columns=columns)

    # 새로운 엑셀 파일로 저장
    with pd.ExcelWriter(output_xlsx_name, engine='xlsxwriter') as writer:
        df_combined.to_excel(writer, index=False, sheet_name='Sheet1') #위에서 생성한 df_combined를 그대로 엑셀에 넣음 (순서 일치)

        # 엑셀 파일의 WorkSheet 객체 가져오기
        worksheet = writer.sheets['Sheet1']

        # A열의 넓이를 14로 설정
        worksheet.set_column('A:A', 14)

        # B열과 C열의 넓이를 최대한 줄여주기
        worksheet.set_column('B:C', None, None, {'hidden': True})

        # D, E, F, G, H, I열의 넓이를 15로 설정하고 통화 형식도 적용
        money_format = writer.book.add_format({'num_format': '$#,##0'})
        worksheet.set_column('D:I', 15, money_format)

    print(f"Data retrieval successful and saved to {output_xlsx_name}!")




    ######## HTML 생성중 #########
    
    
    
    
    # 생성된 엑셀 데이터 읽어오기
    df = pd.read_excel(output_xlsx_name)
    df = df.drop(columns=['CG_id', 'CMC_id'])  # CG_id와 CMC_id 열을 제거

    # 결측값 처리
    df.fillna(0, inplace=True)  

    # pandas DataFrame을 HTML로 변환하기 전에 적용할 통화 형식
    df['CG_MarketCap'] = df['CG_MarketCap'].apply(lambda x: f"${int(x):,}")
    df['CG_FDV'] = df['CG_FDV'].apply(lambda x: f"${int(x):,}")
    df['CMC_MarketCap'] = df['CMC_MarketCap'].apply(lambda x: f"${int(x):,}")
    df['CMC_FDV'] = df['CMC_FDV'].apply(lambda x: f"${int(x):,}")
    df['Binance_OI'] = df['Binance_OI'].apply(lambda x: f"${int(x):,}")
    df['Bybit_OI'] = df['Bybit_OI'].apply(lambda x: f"${int(x):,}")
    df['HL_OI'] = df['HL_OI'].apply(lambda x: f"${int(x):,}")  # HL_OI 통화 형식 추가

    df = df.reindex(columns=['Ticker', 'Upbit_KRW', 'Upbit_BTC', 'Bithumb', 'Coinbase_Spot', 'Binance_Spot', 
                             'Binance_Future', 'Bybit_Future', 'Okx_Future', 'HL_Future',
                             'CG_MarketCap', 'CG_FDV', 'CMC_MarketCap', 'CMC_FDV', 
                             'Binance_OI', 'Bybit_OI', 'HL_OI'])  # HL_OI 추가

    df.rename(columns={
        'Upbit_KRW' : 'Ub_KRW',
        'Upbit_BTC' : 'Ub_BTC',
        'Bithumb' : 'Bithumb',
        'Coinbase_Spot' : 'CB_Spot',
        'Binance_Spot' : 'BN_Spot',
        'Binance_Future' : 'BN_USDM',
        'Bybit_Future' : 'BB_USDM',
        'Okx_Future' : 'OKX_Perp',
        'HL_Future' : 'HL',  # HL_Perp에서 HL로 변경
        'CG_MarketCap': 'CG_MC',
        'CMC_MarketCap': 'CMC_MC',
        'CG_FDV': 'CG_FDV',
        'CMC_FDV': 'CMC_FDV',
        'Binance_OI' : 'Binance_OI',
        'Bybit_OI' : 'Bybit_OI',
        'HL_OI' : 'HL_OI',
        }, inplace=True)

    # 행 번호를 별도의 열로 만들기
    df.reset_index(inplace=True)
    # index열의 제목은 공란으로 만들기
    df.rename(columns={'index': ''}, inplace=True)

    # HTML 코드로 변환
    html = df.to_html(classes='dataframe', index=False)  # index=False 추가

    # HTML 파일로 저장
    with open(output_html_name, 'w', encoding='utf-8') as f:
        f.write('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Researchan's_listing_Info</title>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    }}
                .dataframe {{
                    width: 95%;
                    height: 80%;
                    }}
                .dataTables_wrapper {{
                    width: 95%;
                    margin: auto;
                }}
                h1 {{
                    color: blue;
                    font-size: 24px;
                    text-align:center;
                }}
                label.checkbox-label {{
                margin-right: 10px;
                }}
                
                th{{
                text-align:center;
                }}
                
                th select{{
                display: block;
                margin: 0 auto;
                }}
                
                tbody tr td:nth-child(3),tbody tr td:nth-child(4),
                tbody tr td:nth-child(5),tbody tr td:nth-child(6),
                tbody tr td:nth-child(7),tbody tr td:nth-child(8), 
                tbody tr td:nth-child(9),tbody tr td:nth-child(10),
                {{
                    text-align: center;
                }}
            </style>
            
            <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.css">
            <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
            <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.js"></script>
            
        </head>
        <body>
            <h1>Researchan's listing Info Page</h1>
            <div class="dataTables_wrapper">
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn2" checked> 업빗 KRW
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn3" checked> 업빗 BTC
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn4" checked> 빗썸
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn5" checked> 코인베이스 현물
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn6" checked> 바이낸스 현물
                </label>                
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn7" checked> 바이낸스 선물
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn8" checked> 바이비트 선물
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn9" checked> OKX 선물
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn10" checked> HL
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn11" checked> CG_MC
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn12" checked> CG_FDV
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn13" checked> CMC_MC
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn14" checked> CMC_FDV
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn15" checked> OI_Binance
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn16" checked> OI_Bybit
                </label>
                <label class="checkbox-label">
                    <input type="checkbox" id="toggleColumn17" checked> OI_HL
                </label>
                {table}
            </div>
            <script>
                $(document).ready( function () 
                {{ 
                    // 체크박스 상태에 따라 컬럼 보이기/숨기기
                    $('#toggleColumn2').on('change', function () 
                    {{
                        table.column(2).visible(this.checked);
                    }});
                    $('#toggleColumn3').on('change', function () 
                    {{
                        table.column(3).visible(this.checked);
                    }});
                    $('#toggleColumn4').on('change', function () 
                    {{
                        table.column(4).visible(this.checked);
                    }});
                    $('#toggleColumn5').on('change', function () 
                    {{
                        table.column(5).visible(this.checked);
                    }});
                    $('#toggleColumn6').on('change', function () 
                    {{
                        table.column(6).visible(this.checked);
                    }});
                    $('#toggleColumn7').on('change', function () 
                    {{
                        table.column(7).visible(this.checked);
                    }});
                    $('#toggleColumn8').on('change', function () 
                    {{
                        table.column(8).visible(this.checked);
                    }});
                    $('#toggleColumn9').on('change', function () 
                    {{
                        table.column(9).visible(this.checked);
                    }});
                    $('#toggleColumn10').on('change', function () 
                    {{
                        table.column(10).visible(this.checked);
                    }});
                    $('#toggleColumn11').on('change', function () 
                    {{
                        table.column(11).visible(this.checked);
                    }});
                    $('#toggleColumn12').on('change', function () 
                    {{
                        table.column(12).visible(this.checked);
                    }});
                    $('#toggleColumn13').on('change', function () 
                    {{
                        table.column(13).visible(this.checked);
                    }});
                    $('#toggleColumn14').on('change', function () 
                    {{
                        table.column(14).visible(this.checked);
                    }});
                    $('#toggleColumn15').on('change', function () 
                    {{
                        table.column(15).visible(this.checked);
                    }});
                    $('#toggleColumn16').on('change', function () 
                    {{
                        table.column(16).visible(this.checked);
                    }});
                    $('#toggleColumn17').on('change', function () 
                    {{
                        table.column(17).visible(this.checked);
                    }});
                    
                    
                    var table = $('.dataframe').DataTable(
                    {{    
                        initComplete: function () 
                        {{
                            // 3열에 드롭다운 메뉴 추가
                            this.api().columns(2).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );

                            // 4열에 드롭다운 메뉴 추가
                            this.api().columns(3).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );
                            
                            // 5열에 드롭다운 메뉴 추가
                            this.api().columns(4).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );

                            // 6열에 드롭다운 메뉴 추가 (코인베이스)
                            this.api().columns(5).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );
                            
                            // 7열에 드롭다운 메뉴 추가          
                            this.api().columns(6).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );
                            
                            // 8열에 드롭다운 메뉴 추가          
                            this.api().columns(7).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );
                
                            // 9열에 드롭다운 메뉴 추가          
                            this.api().columns(8).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );   

                            // 10열에 드롭다운 메뉴 추가 (OKX)         
                            this.api().columns(9).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
                                    select.append( '<option value="'+d+'">'+d+'</option>' )
                                }} );
                            }} );   

                            // 11열에 드롭다운 메뉴 추가 (HL)         
                            this.api().columns(10).every( function () 
                            {{
                                var column = this;
                                var select = $(
                                '<select><option value="">전체</option></select>'
                                )
                                    .appendTo( $(column.header()) )
                                    .on( 'change', function () 
                                    {{
                                        var val = $.fn.dataTable.util.escapeRegex(
                                            $(this).val()
                                        );

                                        column
                                            .search( val ? '^'+val+'$' : '', true, false )
                                            .draw();
                                    }} );

                                column.data().unique().sort().each( function ( d, j ) 
                                {{
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
                        "columnDefs": 
                        [{{
                            "searchable": false,
                            "orderable": false,
                            "targets": 0 
                        }}],
                        "columns": 
                        [
                            {{ "width": "10px" }},  // 번호
                            {{ "width": "50px" }},  // Ticker
                            {{ "width": "50px" }},  // Ub_KRW
                            {{ "width": "50px" }},  // Ub_BTC
                            {{ "width": "50px" }},  // Bithumb
                            {{ "width": "50px" }},  // CB_Spot
                            {{ "width": "50px" }},  // BN_Spot
                            {{ "width": "50px" }},  // BN_USDM
                            {{ "width": "50px" }},  // BB_USDM
                            {{ "width": "50px" }},  // OKX_Perp
                            {{ "width": "50px" }},  // HL
                            {{ "width": "80px" }},  // CG_MC
                            {{ "width": "80px" }},  // CG_FDV
                            {{ "width": "80px" }},  // CMC_MC
                            {{ "width": "80px" }},  // CMC_FDV
                            {{ "width": "80px" }},  // Binance_OI
                            {{ "width": "80px" }},  // Bybit_OI
                            {{ "width": "80px" }},  // HL_OI
                        ]
                    }});

                    // This will add numbers on the leftmost column
                    table.on( 'order.dt search.dt', function () 
                    {{
                        table.column(0, {{search:'applied', order:'applied'}}).nodes().each( function (cell, i) 
                        {{cell.innerHTML = i+1;}});
                    }}).draw();
                }});
            </script>
        </body>
        </html>
        '''.format(table=html))

    print(f"Data retrieval successful and saved to {output_html_name}!")

except Exception as e:
    print(e)
    jandimodule.Exchange_Listing_send_message_to_jandi(str(e))
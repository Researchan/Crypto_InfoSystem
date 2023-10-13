import requests
import pandas as pd
import jandimodule

input_file_name = 'ListingDatas.xlsx'
output_xlsx_name = 'Dataoutput.xlsx'
output_html_name = 'ListingDatas.html'

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

df = df.reindex(columns=['Ticker', 'Upbit_KRW', 'Upbit_BTC', 'Bithumb', 'Binance_Future', 'Bybit_Future', 'CG_MarketCap', 'CG_FDV', 'CMC_MarketCap', 'CMC_FDV', 'Binance_OI', 'Bybit_OI'])

df.rename(columns={
    'Upbit_KRW' : 'Ub_KRW',
    'Upbit_BTC' : 'Ub_BTC',
    'Bithumb' : 'Bithumb',
    'Binance_Future' : 'Bn_Usdm',
    'Bybit_Future' : 'Bb_Usdm',
    'CG_MarketCap': 'CG_MC',
    'CMC_MarketCap': 'CMC_MC',
    'CG_FDV': 'CG_FDV',
    'CMC_FDV': 'CMC_FDV',
    'Binance_OI' : 'Binance_OI',
    'Bybit_OI' : 'Bybit_OI'
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
            tbody tr td:nth-child(7) 
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
                <input type="checkbox" id="toggleColumn5" checked> 바이낸스 선물
            </label>
            <label class="checkbox-label">
                <input type="checkbox" id="toggleColumn6" checked> 바이비트 선물
            </label>
            <label class="checkbox-label">
                <input type="checkbox" id="toggleColumn7" checked> CG_MC
            </label>
            <label class="checkbox-label">
                <input type="checkbox" id="toggleColumn8" checked> CG_FDV
            </label>
            <label class="checkbox-label">
                <input type="checkbox" id="toggleColumn9" checked> CMC_MC
            </label>
            <label class="checkbox-label">
                <input type="checkbox" id="toggleColumn10" checked> CMC_FDV
            </label>
            <label class="checkbox-label">
                <input type="checkbox" id="toggleColumn11" checked> OI_Binance
            </label>
            <label class="checkbox-label">
                <input type="checkbox" id="toggleColumn12" checked> OI_Bybit
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
                        
                        // 6열에 드롭다운 메뉴 추가          
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
                        {{ "width": "10px" }},
                        {{ "width": "50px" }},
                        {{ "width": "50px" }},
                        {{ "width": "50px" }},
                        {{ "width": "50px" }},
                        {{ "width": "50px" }},
                        {{ "width": "50px" }},
                        {{ "width": "100px" }},
                        {{ "width": "100px" }},
                        {{ "width": "100px" }},
                        {{ "width": "100px" }},
                        {{ "width": "100px" }},
                        {{ "width": "100px" }},
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
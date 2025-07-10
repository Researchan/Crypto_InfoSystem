import ccxt
import SlackModule

try:
    exBN = ccxt.binance({
        'options': {
            'defaultType': 'spot',
        },
    })
    exBNTickersInfo = exBN.fetchTickers() # 티커 딕셔너리 가져옴
    exBNTickers = exBNTickersInfo.keys() # 티커 키만 받아오기 (이름만)

    #API에서 USDT페어의 티커만 받아오기
    API_Tickerlist = []
    for i in exBNTickers:
        if '/USDT' in i:
            coinname = i.split('/')[0]
            API_Tickerlist.append(coinname)

    #기존에 상장폐지된 리스트 수동으로 제거 (바이낸스가 API에서 여전히 제공해서 수동으로 제거해야함 근데 이 api가 있을텐데..)
    #왜 지들이 리브랜딩 해놓고 처 안지우냐 짜증나게
    delete_list = ['1INCHDOWN', '1INCHUP', 'AAVEDOWN', 'AAVEUP', 'ADADOWN', 'ADAUP', 
                   'AION', 'ANC', 'ANY', 'AUD', 'AUTO', 'BCC', 'BCHABC', 'BCHDOWN', 'BCHUP', 
                   'BEAM', 'BEAR', 'BETH', 'BKRW', 'BNBBEAR', 'BNBBULL', 'BNBDOWN', 'BNBUP', 
                   'BSV', 'BTCDOWN', 'BTCST', 'BTCUP', 'BTG', 'BTT', 'BULL', 'BZRX', 'COCOS', 
                   'DAI', 'DNT', 'DOTDOWN', 'DOTUP', 'EOSBEAR', 'EOSBULL', 'EOSDOWN', 'EOSUP', 
                   'EPS', 'ERD', 'ETHBEAR', 'ETHBULL', 'ETHDOWN', 'ETHUP', 'FILDOWN', 'FILUP', 
                   'GTO', 'GXS', 'HC', 'HNT', 'KEEP', 'LEND', 'LINKDOWN', 'LINKUP', 'LTCDOWN', 'LTCUP', 
                   'MCO', 'MFT', 'MIR', 'MITH', 'NANO', 'NBS', 'NEBL', 'NPXS', 'NU', 'PAX', 'POLY', 
                   'RAMP', 'REP', 'RGT', 'SRM', 'STORM', 'STRAT', 'SUSD', 'SUSHIDOWN', 'SUSHIUP', 
                   'SXPDOWN', 'SXPUP', 'TCT', 'TORN', 'TRIBE', 'TRXDOWN', 'TRXUP', 'UNIDOWN', 'UNIUP', 
                   'USDS', 'USDSB', 'UST', 'VEN', 'XLMDOWN', 'XLMUP', 'XRPBEAR', 'XRPBULL', 
                   'XRPDOWN', 'XRPUP', 'XTZDOWN', 'XTZUP', 'XZC', 'YFIDOWN', 'YFII', 'YFIUP',
                   'MC', 'DREP', 'BTS', 'MOB', 'PERL', 'WTC', 'BUSD', 'ANT', 'DOCK', 'GAL', 'MDX', 'POLS',
                   'EPX', 'EURI', 'REEF', 'BOND','ORN', 'UNFI', 'OOKI', 'FOR', 'VGX', 'KP3R',
                   'CVP', 'KLAY', 'BLZ', 'DAR', 'KEY', 'OAX', 'REEF', 'AKRO','GFT','AMB','REN','WRX',
                   'STMX','LIT', 'BNX', 'COMBO', 'AERGO', 'LINA']




    #바낸 상장되어있는 Spot USDT페어 목록
    Tickerlist = set(API_Tickerlist) - set(delete_list)
    Tickerlist = list(Tickerlist)

    #WBETH, WBTC, EUR, GBP, AEUR 제거
    Tickerlist.remove('WBETH')
    Tickerlist.remove('WBTC')
    Tickerlist.remove('EUR')
    Tickerlist.remove('GBP')
    Tickerlist.remove('AEUR')
    Tickerlist.remove('USD1')
    Tickerlist.remove('PNT')
    Tickerlist.remove('MULTI')
    Tickerlist.remove('PLA')
    Tickerlist.remove('OMG')
    Tickerlist.remove('WNXM')
    Tickerlist.remove('WAVES')
    Tickerlist.remove('XEM')
    Tickerlist.remove('MATIC') #POL로 변했는데 자꾸 이 티커도 정보를 주네 짜증나게. 바이낸스 병신.
    Tickerlist.remove('FTM') #S로 변했는데 자꾸 이 티커도 정보를 주네 짜증나게. 바이낸스 병신.
    Tickerlist.remove('AGIX') # FET합병
    Tickerlist.remove('OCEAN') # FET 합병
    # Tickerlist.remove('SCR') # 임시 보류
    Tickerlist.remove('XUSD') # Stable제외
    # Tickerlist.remove('FORM') # 코개코가 안줘서 임시제외
    Tickerlist.remove('BNSOL')
    # Tickerlist.remove('EPIC') #리브랜딩인데 잠깐 냅두겠음.
    # Tickerlist.remove('LUMIA') #ORN 리브랜딩, 코개코가 안줘서 잠시 없앰.

    #LUNA는 LUNA2로 티커이름 통일하겠음.
    Tickerlist.remove('LUNA')
    Tickerlist.append('LUNA2')

    #SATS정리
    Tickerlist.remove('1000SATS')
    Tickerlist.append('SATS')

    #BTTC는 BTT로 티커이름 통일하겠음.
    Tickerlist.remove('BTTC')
    Tickerlist.append('BTT')

    #BEAMX는 BEAM로 티커이름 통일하겠음.
    Tickerlist.remove('BEAMX')
    Tickerlist.append('BEAM')

    #TOMO 리브랜딩
    Tickerlist.remove('TOMO')
    Tickerlist.append('VIC')

    #TVK 리브랜딩
    Tickerlist.remove('TVK')
    Tickerlist.append('VANRY')

    #RON 티커 정리/
    Tickerlist.remove('RONIN')
    Tickerlist.append('RON')

    #RNDR 티커 정리/
    Tickerlist.remove('RNDR')
    Tickerlist.append('RENDER')

    #RNDR 티커 정리/
    Tickerlist.remove('1MBABYDOGE')
    Tickerlist.append('BABYDOGE')

    Tickerlist.remove('1000CAT')
    Tickerlist.append('CAT')

    Tickerlist.remove('1000CHEEMS') #선물은 상장되어있었네.
    Tickerlist.append('CHEEMS')

    Tickerlist.remove('BROCCOLI714') #선물은 상장되어있었네.
    Tickerlist.append('BROCCOLI')

    #정렬
    Tickerlist.sort()


    # for i in Tickerlist:
    #     print(i)

except Exception as e:
    error_message = f"바이낸스 Spot 데이터 수집 중 오류 발생: {str(e)}"
    print(error_message)
    SlackModule.Exchange_Listing_send_message_to_slack(error_message)
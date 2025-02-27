import ccxt
import jandimodule

try:
    exUpbit = ccxt.upbit({})
    exUpbitTickersInfo = exUpbit.fetchTickers() # 티커 딕셔너리 가져옴
    exUpbitTickers = exUpbitTickersInfo.keys() # 티커 키만 받아오기 (이름만)

    Tickerlist = []
    for i in exUpbitTickers:
        if i[-3:] == 'BTC':
            Tickerlist.append(i[0:-4])

    # Tokamak이 TON이랑 겹침. 또한 오름차순 정렬시 소문자 O를 엑셀이 구분하기때문에 전부 대문자로 변경
    #Tickerlist.remove('Tokamak Network')
    #Tickerlist.append('TOKAMAK')

    
    Tickerlist.remove('USDT') #테더삭제
    Tickerlist.remove('OCEAN') #삭제

    # Tickerlist.remove('LWA') #코인개코에 정보없음. 이제 생김
    Tickerlist.remove('GAME2') #CoinGecko에 정보없음. 얘는 여전히 없음
    # Tickerlist.remove('BOUNTY') #코개코랑 코마캡에 없음
    # Tickerlist.remove('SKY') 
    # Tickerlist.remove('USDS')
    Tickerlist = set(Tickerlist)
    Tickerlist = list(Tickerlist)
    Tickerlist.sort()

    # for i in Tickerlist:
    #     print(i)
    
except Exception as e:
    jandimodule.Exchange_Listing_send_message_to_jandi("upbit BTC오류 : " + str(e))
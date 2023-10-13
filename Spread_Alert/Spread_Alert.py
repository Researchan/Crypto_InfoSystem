import ccxt.async_support as ccxtasync
import ccxt.pro as ccxtpro
import asyncio
import jandimodule
import Get_Tickerlists
import Get_BinanceBybitTicker

sleeptime = 20
interval_init =[1.005] + [round(1000*(1.015 + i * 0.015))/1000 for i in range(39)]
isrange_init = [0 for _ in range(40)]

class Get_Orderbooks:
    def __init__(self, exchange1, exchange2, pair):
        #Binance 현물과 선물의 인스턴스 생성 (페어는 인스턴스 생성시 파라미터로 받음)
        global sleeptime
        global interval_init
        global isrange_init
        self.exchange1 = exchange1
        self.exchange2 = exchange2
        self.pair = pair

    async def fetch_order_books(self):
        #현물과 선물의 오더북 호가를 받아오기
        self.intervals = interval_init
        self.isrange = isrange_init
        self.isrange[0] = 1
        while True:
            try:
                spotticker, futureticker = await asyncio.gather(self.exchange1.watch_ticker(self.pair, params={'name': 'bookTicker'}),
                                                                self.exchange2.watch_ticker(self.pair, params={'name': 'bookTicker'}))
                
                Spot_to_Future_ratio = spotticker['bid']/futureticker['ask'] #SPot에서 bid로 받는 이유는, 누군가 Spot잘못긁어서 Spot매도호가가 비어버릴 경우, 알람이 오작동하는 것을 방지하기위해서.
                
                #1.005이하일 경우
                if (Spot_to_Future_ratio < self.intervals[0]) and (self.isrange[0] != 1):
                    # jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' ' + str((round((self.intervals[0]-1)*1000))/10) + '% 이하\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    self.isrange = [0] * 40
                    self.isrange[0] = 1
                
                #1.005이상부터
                for i in range(1,39):
                    if (self.intervals[i-1] < Spot_to_Future_ratio < self.intervals[i]) and (self.isrange[i] != 1):
                        # jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' ' + str((round((self.intervals[i-1]-1)*1000))/10) + '% 이상 \n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                        jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                        self.isrange = [0] * 40
                        self.isrange[i] = 1

                if (self.intervals[39] < Spot_to_Future_ratio) :
                    # jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' ' + str((round((self.intervals[39]-1)*1000))/10) + ' % 이상\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    
                
                await asyncio.sleep(sleeptime)
            except Exception as e:
                print(e)

    async def close_connections(self):
        await self.exchange1.close()
        await self.exchange2.close()

class Get_1000_Orderbooks:
    def __init__(self, exchange1, exchange2, usdmpair):
        #Binance 현물과 선물의 인스턴스 생성 (페어는 인스턴스 생성시 파라미터로 받음)
        global sleeptime
        global interval_init
        global isrange_init
        self.exchange1 = exchange1
        self.exchange2 = exchange2
        self.spotpair = usdmpair[4:]
        self.usdmpair = usdmpair
        
    async def fetch_order_books(self):
        #현물과 선물의 오더북 호가를 받아오기
        self.intervals = interval_init
        self.isrange = isrange_init
        self.isrange[0] = 1
        while True:
            try:
                spotticker, futureticker = await asyncio.gather(self.exchange1.watch_ticker(self.spotpair, params={'name': 'bookTicker'}),
                                                                self.exchange2.watch_ticker(self.usdmpair, params={'name': 'bookTicker'}))
                
                Spot_to_Future_ratio = spotticker['bid']/futureticker['ask'] #SPot에서 bid로 받는 이유는, 누군가 Spot잘못긁어서 Spot매도호가가 비어버릴 경우, 알람이 오작동하는 것을 방지하기위해서.
                
                #1.005이하일 경우
                if (Spot_to_Future_ratio < self.intervals[0]) and (self.isrange[0] != 1):
                    # jandimodule.Alert_send_message_to_jandi(str(self.spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    jandimodule.Alert_send_message_to_jandi(str(self.spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    self.isrange = [0] * 40
                    self.isrange[0] = 1
                
                #1.005이상부터
                for i in range(1,39):
                    if (self.intervals[i-1] < Spot_to_Future_ratio < self.intervals[i]) and (self.isrange[i] != 1):
                        # jandimodule.Alert_send_message_to_jandi(str(self.spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                        jandimodule.Alert_send_message_to_jandi(str(self.spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                        self.isrange = [0] * 40
                        self.isrange[i] = 1

                if (self.intervals[39] < Spot_to_Future_ratio) :
                    # jandimodule.Alert_send_message_to_jandi(str(self.spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    jandimodule.Alert_send_message_to_jandi(str(self.spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    
                
                await asyncio.sleep(sleeptime)
            except Exception as e:
                print(e)

    async def close_connections(self):
        await self.exchange1.close()
        await self.exchange2.close()

class Get_Luna_Orderbooks:
    def __init__(self, exchange1, exchange2, Spotpair, Futurepair):
        #Binance 현물과 선물의 인스턴스 생성 (페어는 인스턴스 생성시 파라미터로 받음)
        global sleeptime
        global interval_init
        global isrange_init
        self.exchange1 = exchange1
        self.exchange2 = exchange2
        self.Spotpair = Spotpair
        self.Futurepair = Futurepair

    async def fetch_order_books(self):
        #현물과 선물의 오더북 호가를 받아오기
        self.intervals = interval_init
        self.isrange = isrange_init
        self.isrange[0] = 1
        while True:
            try:
                spotticker, futureticker = await asyncio.gather(self.exchange1.watch_ticker(self.Spotpair, params={'name': 'bookTicker'}),
                                                                self.exchange2.watch_ticker(self.Futurepair, params={'name': 'bookTicker'}))
                
                Spot_to_Future_ratio = spotticker['bid']/futureticker['ask'] #SPot에서 bid로 받는 이유는, 누군가 Spot잘못긁어서 Spot매도호가가 비어버릴 경우, 알람이 오작동하는 것을 방지하기위해서.
                
                #1.005이하일 경우
                if (Spot_to_Future_ratio < self.intervals[0]) and (self.isrange[0] != 1):
                    jandimodule.Alert_send_message_to_jandi(str(self.Spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    self.isrange = [0] * 40
                    self.isrange[0] = 1
                
                #1.005이상부터
                for i in range(1,39):
                    if (self.intervals[i-1] < Spot_to_Future_ratio < self.intervals[i]) and (self.isrange[i] != 1):
                        jandimodule.Alert_send_message_to_jandi(str(self.Spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                        self.isrange = [0] * 40
                        self.isrange[i] = 1

                if (self.intervals[39] < Spot_to_Future_ratio) :
                    jandimodule.Alert_send_message_to_jandi(str(self.Spotpair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    
                
                await asyncio.sleep(sleeptime)
            except Exception as e:
                print(e)

    async def close_connections(self):
        await self.exchange1.close()
        await self.exchange2.close()

class Get_BinanceBybit_Orderbooks:
    def __init__(self, exchange1, exchange2, pair):
        #바이낸스 현물과 바이비트 선물의 인스턴스 생성 (페어는 인스턴스 생성시 파라미터로 받음)
        global sleeptime
        global interval_init
        global isrange_init
        self.exchange1 = exchange1
        self.exchange2 = exchange2
        self.BinanceSpot_pair = pair[0:-5]
        self.BybitFuture_pair = pair

    async def fetch_order_books(self):
        #현물과 선물의 오더북 호가를 받아오기
        self.intervals = interval_init
        self.isrange = isrange_init
        self.isrange[0] = 1
        while True:
            try:
                spotticker, futureticker = await asyncio.gather(self.exchange1.watch_ticker(self.BinanceSpot_pair, params={'name': 'bookTicker'}),
                                                                self.exchange2.watch_ticker(self.BybitFuture_pair, params={'name': 'bookTicker'}))
                
                Spot_to_Future_ratio = spotticker['bid']/futureticker['ask'] #SPot에서 bid로 받는 이유는, 누군가 Spot잘못긁어서 Spot매도호가가 비어버릴 경우, 알람이 오작동하는 것을 방지하기위해서.
                
                #1.005이하일 경우
                if (Spot_to_Future_ratio < self.intervals[0]) and (self.isrange[0] != 1):
                    # jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' ' + str((round((self.intervals[0]-1)*1000))/10) + '% 이하\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    jandimodule.Alert_send_message_to_jandi('BYBIT\n' + str(self.BinanceSpot_pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    self.isrange = [0] * 40
                    self.isrange[0] = 1
                
                #1.005이상부터
                for i in range(1,39):
                    if (self.intervals[i-1] < Spot_to_Future_ratio < self.intervals[i]) and (self.isrange[i] != 1):
                        # jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' ' + str((round((self.intervals[i-1]-1)*1000))/10) + '% 이상 \n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                        jandimodule.Alert_send_message_to_jandi('BYBIT\n' + str(self.BinanceSpot_pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                        self.isrange = [0] * 40
                        self.isrange[i] = 1

                if (self.intervals[39] < Spot_to_Future_ratio) :
                    # jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' ' + str((round((self.intervals[39]-1)*1000))/10) + ' % 이상\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    jandimodule.Alert_send_message_to_jandi('BYBIT\n' + str(self.BinanceSpot_pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio-1))/100) + '%')
                    
                
                await asyncio.sleep(sleeptime)
            except Exception as e:
                print(e)

    async def close_connections(self):
        await self.exchange1.close()
        await self.exchange2.close()


async def main():
    
    Tickers_main = Get_Tickerlists.Tickerlist
    Tickers_1000pair = Get_Tickerlists.future1000_Tickerlist
    Tickers_Luna = Get_Tickerlists.Luna_Tickerlist
    Tickers_Binance_Bybit = Get_BinanceBybitTicker.Tickerlist # BTT가 생략되는데, 그냥 스프레드도 너무크고 이상해서 버려도 될듯.

    instance_dict = {}
    exBN = ccxtpro.binance({})
    exBNfuture = ccxtpro.binanceusdm({})
    exBybit = ccxtpro.bybit({})
    
    try:
        #처음 소켓 연결시키기
        await exBN.watch_ticker('BTC/USDT')
        await exBNfuture.watch_ticker('BTC/USDT')
        await exBybit.watch_ticker('BTC/USDT:USDT')
        
        #바이낸스 현선티커 등록
        for Ticker in Tickers_main:
            instance_dict[str(Ticker)] = Get_Orderbooks(exBN, exBNfuture, Ticker)
            print(Ticker, '인스턴스 생성완료')
        
        #바이낸스 1000Perps 현선티커 등록
        for Ticker in Tickers_1000pair:
            instance_dict[str(Ticker)] = Get_1000_Orderbooks(exBN, exBNfuture, Ticker)
            print(Ticker, '인스턴스 생성완료')
        
        #바이낸스현물, 바이빗선물(바이낸스 선물에 없는)
        for Ticker in Tickers_Binance_Bybit:
            instance_dict[str(Ticker)] = Get_BinanceBybit_Orderbooks(exBN, exBybit, Ticker)
            print('바이빗 : ', Ticker, '인스턴스 생성완료')
            
        #바이낸스 루나 티커 등록
        instance_dict['LUNA/USDT'] = Get_Luna_Orderbooks(exBN, exBNfuture, Tickers_Luna[0], Tickers_Luna[1])
        print('LUNA/USDT', '인스턴스 생성완료')
    
        
            
            
            
        tasks = [instance.fetch_order_books() for instance in instance_dict.values()]
        await asyncio.gather(*tasks)
        
    except Exception as e:
        jandimodule.acc2_send_message_to_jandi('바이낸스 현선갭 알람 에러 : ' + str(e))

    finally:
        await exBN.close()
        await exBNfuture.close()
        await exBybit.close()
    
    
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
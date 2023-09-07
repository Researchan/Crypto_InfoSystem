import ccxt.async_support as ccxtasync
import ccxt.pro as ccxtpro
import asyncio
import time
import ccxt
import jandimodule
import Binancelist

class Get_Orderbooks:
    def __init__(self, exchange1, exchange2, pair):
        #Binance 현물과 선물의 인스턴스 생성 (페어는 인스턴스 생성시 파라미터로 받음)
        self.exchange1 = exchange1
        self.exchange2 = exchange2
        self.pair = pair

    async def fetch_order_books(self):
        #현물과 선물의 오더북 호가를 받아오기
        self.intervals = [round(1000*(1.005 + i * 0.005))/1000 for i in range(40)]
        self.isrange = [0 for _ in range(40)]
        self.isrange[0] = 1
        while True:
            try:
                spotticker, futureticker = await asyncio.gather(self.exchange1.watch_ticker(self.pair, params={'name': 'bookTicker'}),
                                                                self.exchange2.watch_ticker(self.pair, params={'name': 'bookTicker'}))
                
                Spot_to_Future_ratio = spotticker['bid']/futureticker['ask'] #SPot에서 bid로 받는 이유는, 누군가 Spot잘못긁어서 Spot매도호가가 비어버릴 경우, 알람이 오작동하는 것을 방지하기위해서.
                
                #1.005이하일 경우
                if (Spot_to_Future_ratio < self.intervals[0]) and (self.isrange[0] != 1):
                    jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' 0.5% 이하\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    self.isrange = [0] * 40
                    self.isrange[0] = 1
                
                #1.005이상부터
                for i in range(1,39):
                    if (self.intervals[i-1] < Spot_to_Future_ratio < self.intervals[i]) and (self.isrange[i] != 1):
                        jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' ' + str((round((self.intervals[i-1]-1)*1000))/10) + '% 이상 \n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                        self.isrange = [0] * 40
                        self.isrange[i] = 1

                if (self.intervals[39] < Spot_to_Future_ratio) :
                    jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + ' 20% 이상\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    
                
                await asyncio.sleep(5)
            except Exception as e:
                print(e)

    async def close_connections(self):
        await self.exchange1.close()
        await self.exchange2.close()

class Get_1000Orderbooks:
    def __init__(self, exchange1, exchange2, pair):
        #Binance 현물과 선물의 인스턴스 생성 (페어는 인스턴스 생성시 파라미터로 받음)
        self.exchange1 = exchange1
        self.exchange2 = exchange2
        self.spotpair = pair[4:]
        self.usdmpair = pair
        
    async def fetch_order_books(self):
        #현물과 선물의 오더북 호가를 받아오기
        self.intervals = [round(1000*(1.005 + i * 0.005))/1000 for i in range(40)]
        self.isrange = [0 for _ in range(40)]
        self.isrange[0] = 1
        while True:
            try:
                spotticker, futureticker = await asyncio.gather(self.exchange1.watch_ticker(self.spotpair, params={'name': 'bookTicker'}),
                                                                self.exchange2.watch_ticker(self.usdmpair, params={'name': 'bookTicker'}))
                
                Spot_to_Future_ratio = spotticker['bid']/futureticker['ask'] #SPot에서 bid로 받는 이유는, 누군가 Spot잘못긁어서 Spot매도호가가 비어버릴 경우, 알람이 오작동하는 것을 방지하기위해서.
                
                #1.005이하일 경우
                if (Spot_to_Future_ratio < self.intervals[0]) and (self.isrange[0] != 1):
                    jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    self.isrange = [0] * 40
                    self.isrange[0] = 1
                
                #1.005이상부터
                for i in range(1,39):
                    if (self.intervals[i-1] < Spot_to_Future_ratio < self.intervals[i]) and (self.isrange[i] != 1):
                        jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                        self.isrange = [0] * 40
                        self.isrange[i] = 1

                if (self.intervals[39] < Spot_to_Future_ratio) :
                    jandimodule.Alert_send_message_to_jandi(str(self.pair)[0:-5] + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    
                
                await asyncio.sleep(5)
            except Exception as e:
                print(e)

    async def close_connections(self):
        await self.exchange1.close()
        await self.exchange2.close()

class Get_LunaOrderbooks:
    def __init__(self, exchange1, exchange2):
        #Binance 현물과 선물의 인스턴스 생성 (페어는 인스턴스 생성시 파라미터로 받음)
        self.exchange1 = exchange1
        self.exchange2 = exchange2

    async def fetch_order_books(self):
        #현물과 선물의 오더북 호가를 받아오기
        self.intervals = [round(1000*(1.005 + i * 0.005))/1000 for i in range(40)]
        self.isrange = [0 for _ in range(40)]
        self.isrange[0] = 1
        
        while True:
            try:
                spotticker, futureticker = await asyncio.gather(self.exchange1.watch_ticker('LUNA/USDT', params={'name': 'bookTicker'}),
                                                                self.exchange2.watch_ticker('LUNA2/USDT', params={'name': 'bookTicker'}))
                
                Spot_to_Future_ratio = spotticker['bid']/futureticker['ask'] #SPot에서 bid로 받는 이유는, 누군가 Spot잘못긁어서 Spot매도호가가 비어버릴 경우, 알람이 오작동하는 것을 방지하기위해서.
                
                #1.005이하일 경우
                if (Spot_to_Future_ratio < self.intervals[0]) and (self.isrange[0] != 1):
                    jandimodule.Alert_send_message_to_jandi('LUNA' + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    self.isrange = [0] * 40
                    self.isrange[0] = 1
                
                #1.005이상부터
                for i in range(1,39):
                    if (self.intervals[i-1] < Spot_to_Future_ratio < self.intervals[i]) and (self.isrange[i] != 1):
                        jandimodule.Alert_send_message_to_jandi('LUNA' + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                        self.isrange = [0] * 40
                        self.isrange[i] = 1

                if (self.intervals[39] < Spot_to_Future_ratio) :
                    jandimodule.Alert_send_message_to_jandi('LUNA' + '\n' + str(round(10000*(Spot_to_Future_ratio))/10000))
                    
                
                await asyncio.sleep(5)
            except Exception as e:
                print(e)

    async def close_connections(self):
        await self.exchange1.close()
        await self.exchange2.close()

async def main():
    exBN = ccxt.binance({})
    exBNfuture = ccxt.binanceusdm({})
    
    Tickers_main = Binancelist.Tickerlist
    Tickers_1000pair = Binancelist.future1000pairs
    Tickers_luna = Binancelist.Lunapair

    instance_dict = {}
    exBN = ccxtpro.binance({})
    exBNfuture = ccxtpro.binanceusdm({})
    
    try:
        await exBN.watch_ticker('BTC/USDT')
        await exBNfuture.watch_ticker('BTC/USDT')
        
        for Ticker in Tickers_main:
            instance_dict[str(Ticker)] = Get_Orderbooks(exBN, exBNfuture, Ticker)
            print(Ticker, '인스턴스 생성완료')
            
        for Ticker in Tickers_1000pair:
            instance_dict[str(Ticker)] = Get_1000Orderbooks(exBN, exBNfuture, Ticker)
            print(Ticker, '인스턴스 생성완료')
        
        instance_dict[str(Ticker)] = Get_LunaOrderbooks(exBN, exBNfuture)
            
        tasks = [instance.fetch_order_books() for instance in instance_dict.values()]
        await asyncio.gather(*tasks)
        
    except Exception as e:
        print(e)

    finally:
        await exBN.close()
        await exBNfuture.close()
    
    
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
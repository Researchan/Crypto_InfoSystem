import asyncio
import ccxt.pro as ccxtpro

exBybit = ccxtpro.bybit({})

async def main():
    res = await exBybit.watch_ticker('BTC/USDT:USDT', params={'name': 'bookTicker'})
    print(res)
    
    await exBybit.close()
    
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())    
asyncio.run(main())

# Bybit도 똑같네. 페어만 잘 주면 되겠다.
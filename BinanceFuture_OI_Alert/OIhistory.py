import ccxt

exBNfuture = ccxt.binanceusdm({})

res = exBNfuture.fetch_open_interest_history('BTCUSDT', timeframe='1h', params={
    'limit':'2',
})

print(res[0]['openInterestValue'])
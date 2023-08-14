from coinmarketcap import Market
coinmarketcap = Market()

res = coinmarketcap.ticker(1, convert='EUR')
print(res)
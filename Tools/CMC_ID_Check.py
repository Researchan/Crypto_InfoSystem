import requests

apikey = '339f7745-0a39-4c98-924a-39f07902c361'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apikey,
}

parameters = {
    'listing_status' : 'active',
    'start' : 1,
    'limit' : 5000,
    'sort' : 'cmc_rank',
}

# Send HTTP GET request
response = requests.get(url, headers=headers, params=parameters)

symbols = [
    "LADYS", "BONK", "AKRO", "ALPACA", "BICO", "BSW", "BUSD", "CEEK", "CORE",
    "ETHW", "FORTH", "GFT", "GLMR", "HNT", "ILV", "KAS", "KDA", "LOOKS", "ORDI",
    "PAXG", "SCRT", "SLP", "SWEAT", "TWT", "VGX", "XNO"
]
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response data in JSON format
    res = response.json()
    data = res['data']
    datalist = list(data)
    printlist = []
        
    for i in range(0,len(datalist)):
        for symbol in symbols:
            if datalist[i]['symbol'] == symbol:
                #print((datalist[i]))
                tempstring = str(symbol) + " : " + str(datalist[i]['id']) + " rank: " + str(datalist[i]['rank'])
                printlist.append(tempstring)
    
    printlist.sort()
    
    for i in printlist:
        print(i)
                
    
else:
    print('error :', response.status_code, response.json())
    

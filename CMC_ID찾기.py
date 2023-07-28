import requests
import ccxt
import json

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

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the response data in JSON format
    res = response.json()
    data = res['data']
    datalist = list(data)
        
    for i in range(0,len(datalist)):
            if datalist[i]['symbol'] == 'ARKM':
                print('ARKM : ', datalist[i]['id'])
                
            if datalist[i]['symbol'] == 'AGLD':
                print('AGLD : ', datalist[i]['id'])
                
            # if datalist[i]['symbol'] == 'NMR':
            #     print('NMR : ', datalist[i]['id'])
                
            # if datalist[i]['symbol'] == 'XVG':
            #     print('XVG : ', datalist[i]['id'])
    
else:
    print('error :', response.status_code, response.json())
    

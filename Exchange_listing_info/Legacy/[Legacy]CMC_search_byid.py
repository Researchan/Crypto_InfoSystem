import requests
import json

# Open the file and load the data
with open('BinanceFuture_id.json', 'r') as file:
    dict_ids = json.load(file)

#listing the data
list_ids = list(dict_ids.values())

#CG와 CMC id 분류
CGlist_ids1 =[]
CGlist_ids2 =[]
CGlist_ids3 =[]
CGlist_ids4 =[]
CMClist_ids1 =[]
CMClist_ids2 =[]
CMClist_ids3 =[]
CMClist_ids4 =[]

#id 리스트 나누기
idcount = 0
for i in list_ids:
    if idcount < 50:
        CGlist_ids1.append(i['CG_id'])
    
    elif idcount < 100:
        CGlist_ids2.append(i['CG_id'])
        
    elif idcount < 150:
        CGlist_ids3.append(i['CG_id'])
    
    elif idcount < 200:
        CGlist_ids4.append(i['CG_id'])
        
    idcount += 1

idcount = 0
for i in list_ids:
    if idcount < 50:
        CMClist_ids1.append(i['CMC_id'])
    
    elif idcount < 100:
        CMClist_ids2.append(i['CMC_id'])
        
    elif idcount < 150:
        CMClist_ids3.append(i['CMC_id'])
    
    elif idcount < 200:
        CMClist_ids4.append(i['CMC_id'])
        
    idcount += 1

# CG와 CMC id String 생성
CG_ids1 = ''
CG_ids2 = ''
CG_ids3 = ''
CG_ids4 = ''

CMC_ids1 = ''
CMC_ids2 = ''
CMC_ids3 = ''
CMC_ids4 = ''

#CG id string화 완료
for i in CGlist_ids1:
    CG_ids1 += i
    CG_ids1 += ','
for i in CGlist_ids2:
    CG_ids2 += i
    CG_ids2 += ','
for i in CGlist_ids3:
    CG_ids3 += i
    CG_ids3 += ','
for i in CGlist_ids4:
    CG_ids4 += i
    CG_ids4 += ','

CG_ids1 = CG_ids1.rstrip(',')
CG_ids2 = CG_ids2.rstrip(',')
CG_ids3 = CG_ids3.rstrip(',')
CG_ids4 = CG_ids4.rstrip(',')

#CMC id string화 완료
for i in CMClist_ids1:
    CMC_ids1 += i
    CMC_ids1 += ','
for i in CGlist_ids2:
    CMC_ids2 += i
    CMC_ids2 += ','
for i in CGlist_ids3:
    CMC_ids3 += i
    CMC_ids3 += ','
for i in CGlist_ids4:
    CMC_ids4 += i
    CMC_ids4 += ','

CMC_ids1 = CMC_ids1.rstrip(',')
CMC_ids2 = CMC_ids2.rstrip(',')
CMC_ids3 = CMC_ids3.rstrip(',')
CMC_ids4 = CMC_ids4.rstrip(',')


# CMC_apikey = '339f7745-0a39-4c98-924a-39f07902c361'
# url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

# headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': CMC_apikey,
# }

# parameters1 = {
#     'id' : id1,
# }

# # Send HTTP GET request
# response = requests.get(url, headers=headers, params=parameters)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     res = response.json()
#     res = res['data']
#     print(res)
    
# else:
#     print('error :', response.status_code, response.json())
    
import json

with open('CG_BinanceFuture_id.json') as file:
    dict_CG = json.load(file)
    
with open('CMC_BinanceFuture_id.json') as file:
    dict_CMC = json.load(file)
    
# print(dict_CG)
# print(dict_CMC)


dict_Tickers = {}

# for i in dict_CG.keys():
#     print(dict_CG[i])



for i in dict_CG.keys():
    dict_Tickers[i]={'CG_id' : dict_CG[i], 
                    'CMC_id' : dict_CMC[i]}

print(dict_Tickers)


with open("BinanceFuture_id.json", "w") as json_file:
    json.dump(dict_Tickers, json_file, indent=0)

print("JSON file created successfully.")

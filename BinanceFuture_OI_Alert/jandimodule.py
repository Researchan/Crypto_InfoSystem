import requests

Webhook_Address1 = "https://wh.jandi.com/connect-api/webhook/27226641/e7b1034711f262a4b424c22b8cbd703c"
Webhook_Address2 = "https://wh.jandi.com/connect-api/webhook/27226641/d751867a5cc74e6cdabfd7176ea03a4b"
Webhook_Address3 = "https://wh.jandi.com/connect-api/webhook/27226641/b1199ced72dc045b8723c52d94cd7a43"
Webhook_Address4 = "https://wh.jandi.com/connect-api/webhook/27226641/594b6fb08461fa95560bc5d13bba6014"
Webhook_Address5 = "https://wh.jandi.com/connect-api/webhook/27226641/35e3029ea8f39016b124cfd0720e2ad6"
Webhook_Address6 = "https://wh.jandi.com/connect-api/webhook/27226641/39612962a364af82d7db9d2a5435b276"

def acc1_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body": message
    }
    requests.post(Webhook_Address1, headers=headers, json=payload)
    
def acc2_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body": message
    }
    requests.post(Webhook_Address2, headers=headers, json=payload)
    
def acc3_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body": message
    }
    requests.post(Webhook_Address3, headers=headers, json=payload)
    
def acc4_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body": message
    }
    requests.post(Webhook_Address4, headers=headers, json=payload)
    
def Alert_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body": message
    }
    requests.post(Webhook_Address5, headers=headers, json=payload)
    
def OI_Alert_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body" : message,
    }
    requests.post(Webhook_Address6, headers=headers, json=payload)
    
#두나무 환율
def get_usd_krw():
    url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
    exchange =requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}).json()
    return exchange[0]['basePrice']
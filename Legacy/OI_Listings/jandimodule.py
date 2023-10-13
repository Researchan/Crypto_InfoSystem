import requests
Webhook_Address1 = "https://wh.jandi.com/connect-api/webhook/27226641/ad086659f319351a97fc4ed7c1d4fccd"
Webhook_Address2 = "https://wh.jandi.com/connect-api/webhook/27226641/39612962a364af82d7db9d2a5435b276"

def Bybit_OI_Alert_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body" : message,
    }
    requests.post(Webhook_Address1, headers=headers, json=payload)
    
def Binance_OI_Alert_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body" : message,
    }
    requests.post(Webhook_Address2, headers=headers, json=payload)
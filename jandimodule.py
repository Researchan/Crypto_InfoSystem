import requests

Webhook_Address1 = "https://wh.jandi.com/connect-api/webhook/27226641/b3a9191223a24ff3a895182714991b5a"
Webhook_Address2 = "https://wh.jandi.com/connect-api/webhook/27226641/35e3029ea8f39016b124cfd0720e2ad6"
Webhook_Address3 = "https://wh.jandi.com/connect-api/webhook/29318137/2168a446ed10093b759617c5b472c99e"

def Exchange_Listing_send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body": message
    }
    requests.post(Webhook_Address1, headers=headers, json=payload)
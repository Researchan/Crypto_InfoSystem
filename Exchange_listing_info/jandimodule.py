import requests

Webhook_Address1 = "https://wh.jandi.com/connect-api/webhook/27226641/e7b1034711f262a4b424c22b8cbd703c"

def send_message_to_jandi(message):
    headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
    }
    payload = {
        "body": message
    }
    requests.post(Webhook_Address1, headers=headers, json=payload)
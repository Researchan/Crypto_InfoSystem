import requests

Webhook_Address1 = "https://wh.jandi.com/connect-api/webhook/27226641/e7b1034711f262a4b424c22b8cbd703c"
Webhook_Address2 = "https://wh.jandi.com/connect-api/webhook/27226641/d751867a5cc74e6cdabfd7176ea03a4b"
Webhook_Address3 = "https://wh.jandi.com/connect-api/webhook/27226641/b1199ced72dc045b8723c52d94cd7a43"
Webhook_Address4 = "https://wh.jandi.com/connect-api/webhook/27226641/594b6fb08461fa95560bc5d13bba6014"
Webhook_Address5 = "https://wh.jandi.com/connect-api/webhook/27226641/35e3029ea8f39016b124cfd0720e2ad6"

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
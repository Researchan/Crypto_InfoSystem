import requests

# 슬랙 웹훅 주소
Webhook_Address = "https://hooks.slack.com/services/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"

def Exchange_Listing_send_message_to_slack(message):
    """
    슬랙으로 메시지를 전송하는 함수
    """
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "text": message,
        "username": "CryptoBot",
        "icon_emoji": ":chart_with_upwards_trend:"
    }
    
    try:
        response = requests.post(Webhook_Address, headers=headers, json=payload)
        if response.status_code == 200:
            print("슬랙 메시지 전송 성공")
        else:
            print(f"슬랙 메시지 전송 실패: {response.status_code}")
            print(f"응답 내용: {response.text}")
            print(f"웹훅 URL: {Webhook_Address}")
    except Exception as e:
        print(f"슬랙 메시지 전송 중 오류: {e}") 
import requests

def send_sms(phone_number, message):
    url = "http://notify.eskiz.uz/api/message/sms/send"

    payload = {'mobile_phone': phone_number,
               'message': message,
               'from': '4546',
               'callback_url': 'http://0000.uz/test.php'}
    files = [

    ]
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjUsInJvbGUiOiJ1c2VyIiwiZGF0YSI6eyJpZCI6NSwibmFtZSI6Ilx1MDQyN1x1MDQxZiBCZXN0IEludGVybmV0IFNvbHV0aW9uIiwiZW1haWwiOiJ0ZXN0QGVza2l6LnV6Iiwicm9sZSI6InVzZXIiLCJhcGlfdG9rZW4iOm51bGwsInN0YXR1cyI6ImFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJiYWxhbmNlIjozMjAwLCJpc192aXAiOjAsImhvc3QiOiJzZXJ2ZXIxIiwiY3JlYXRlZF9hdCI6bnVsbCwidXBkYXRlZF9hdCI6IjIwMjItMDMtMjVUMTk6MzU6MDcuMDAwMDAwWiJ9LCJpYXQiOjE2NDgyNzMzNTYsImV4cCI6MTY1MDg2NTM1Nn0.ZMyJBMR102mdFaBB5GnZrHq9TWCi9s-m7FhCqMaSJUg'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
send_sms('+998907597059','Have you got free time?I am online and i am waiting you my dear')
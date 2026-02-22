import time
import requests
import threading

API_URL = "https://api.seedance.ai/v1/chat/completions"
API_KEY = "YOUR_API_KEY"

payload = {
    "model": "seedance-1.0-pro-fast",
    "messages": [
        {"role": "user", "content": "Write a detailed 1500 word essay about AI technology trends in 2026."}
    ],
    "max_tokens": 1500
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def send_request():
    while True:
        try:
            r = requests.post(API_URL, json=payload, headers=headers)
            print(r.status_code)
        except:
            pass
        time.sleep(0.125)  # 8 requests per second

for _ in range(8):  # 8 parallel workers
    threading.Thread(target=send_request).start()

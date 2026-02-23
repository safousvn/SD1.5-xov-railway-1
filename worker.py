import os
import time
import requests
import threading

API_URL = "https://ark.ap-southeast.bytepluses.com/api/v3/contents/generations/tasks"
API_KEY = os.getenv("ARK_API_KEY", "").strip()

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "seedance-1-0-pro-fast-251015",
    "content": [
       {
        "type": "text",
        "text": "A cinematic futuristic city in 2026, ultra realistic, 4K"
       }
    ],
    "parameters": {
        "duration": 8,
        "resolution": "720p"
    }
}

def send_request():
    while True:
        r = requests.post(API_URL, json=payload, headers=headers)
        print(r.status_code, r.text)
        time.sleep(1)

for _ in range(5):
    threading.Thread(target=send_request).start()

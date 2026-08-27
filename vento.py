import os

import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

CHAT_ID = "8763679403"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {

    "chat_id": CHAT_ID,

    "text": "🌬️ TEST ALLARME VENTO\n\nIl bot Telegram funziona correttamente!"

}

response = requests.post(url, data=data, timeout=20)

print("RISPOSTA TELEGRAM:")

print(response.text)

response.raise_for_status()
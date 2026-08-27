import os

import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

url = f"https://api.telegram.org/bot{TOKEN}/getWebhookInfo"

response = requests.get(url, timeout=20)

print("WEBHOOK TELEGRAM:")

print(response.text)

response.raise_for_status()

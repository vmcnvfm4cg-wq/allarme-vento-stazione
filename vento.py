import os

import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"

response = requests.get(url, timeout=20)

print("RISPOSTA TELEGRAM:")

print(response.text)

response.raise_for_status()

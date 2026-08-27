import os

import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

response = requests.get(url, timeout=20)

print("RISPOSTA TELEGRAM:")

print(response.text)

response.raise_for_status(
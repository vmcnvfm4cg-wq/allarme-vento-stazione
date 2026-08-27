import os

import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

url = f"https://api.telegram.org/bot{TOKEN}/getMe"

response = requests.get(url, timeout=20)

print("BOT COLLEGATO AL TOKEN:")

print(response.text)

response.raise_for_status()

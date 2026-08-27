import os

import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"

response = requests.get(url, timeout=20)

print("RISPOSTA TELEGRAM:")

print(response.text)

response.raise_for_status()

data = response.json()

if data["ok"] and data["result"]:

    for update in data["result"]:

        message = update.get("message", {})

        chat = message.get("chat", {})

        print("CHAT ID:", chat.get("id"))

        print("NOME:", chat.get("first_name"))

        print("MESSAGGIO:", message.get("text"))

else:

    print("NESSUN MESSAGGIO RICEVUTO.")

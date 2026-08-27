import requests

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

print("Controllo token Telegram...")

url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getMe"

response = requests.get(url, timeout=20)

print("RISPOSTA TELEGRAM:", response.text)

response.raise_for_status()

data = response.json()

if data.get("ok"):

    print("✅ TOKEN TELEGRAM VALIDO")

    print("Nome bot:", data["result"].get("first_name"))

    print("Username bot:", data["result"].get("username"))

else:

    print("❌ TOKEN TELEGRAM NON VALIDO")

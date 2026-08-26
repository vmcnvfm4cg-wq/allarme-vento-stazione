import os
import requests

STATION_ID = "IIMPER69"
SOGLIA = 20  # km/h

WU_API_KEY = os.environ["WU_API_KEY"]
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

# Recupera automaticamente il Chat ID dall'ultimo messaggio
updates_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
updates = requests.get(updates_url, timeout=20).json()

if not updates.get("ok") or not updates.get("result"):
    raise Exception("Prima invia /start al bot Telegram")

chat_id = updates["result"][-1]["message"]["chat"]["id"]

# Legge la stazione VEVOR da Weather Underground
url = (
    "https://api.weather.com/v2/pws/observations/current"
    f"?stationId={STATION_ID}"
    "&format=json"
    "&units=m"
    "&numericPrecision=decimal"
    f"&apiKey={WU_API_KEY}"
)

response = requests.get(url, timeout=20)
response.raise_for_status()

data = response.json()
obs = data["observations"][0]

raffica_ms = obs["metric"].get("windGust")

if raffica_ms is None:
    raise Exception("Raffica vento non disponibile")

raffica_kmh = raffica_ms * 3.6

print(f"Raffica rilevata: {raffica_kmh:.1f} km/h")

if raffica_kmh >= SOGLIA:
    messaggio = (
        "🌬️ ALLERTA VENTO VEVOR\n\n"
        f"Raffica: {raffica_kmh:.1f} km/h\n"
        f"Soglia: {SOGLIA} km/h"
    )

    send_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    requests.post(
        send_url,
        json={
            "chat_id": chat_id,
            "text": messaggio
        },
        timeout=20
    )
  

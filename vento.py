import os
import requests

STATION_ID = "IIMPER69"
CHAT_ID = "8763679403"
SOGLIA = 20  # km/h

WU_API_KEY = os.environ["WU_API_KEY"]
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

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

    send_url = (
        f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    )

    telegram_response = requests.post(
        send_url,
        json={
            "chat_id": CHAT_ID,
            "text": messaggio
        },
        timeout=20
    )

    telegram_response.raise_for_status()

    print("Notifica Telegram inviata.")
else:
    print("Vento sotto la soglia.")

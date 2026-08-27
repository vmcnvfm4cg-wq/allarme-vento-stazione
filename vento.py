import os

import json

import requests

STATION_ID = "IIMPER69"

CHAT_ID = "8763679403"

SOGLIA = 20 # km/h

WU_API_KEY = os.environ["WU_API_KEY"]

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

STATE_FILE = "stato.json"

# =========================

# LEGGE LO STATO PRECEDENTE

# =========================

if os.path.exists(STATE_FILE):

    with open(STATE_FILE, "r") as f:

        stato = json.load(f)

else:

    stato = {"allarme_attivo": False}

# =========================

# LEGGE LA VEVOR DA WEATHER UNDERGROUND

# =========================

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

print("DATI VENTO:", obs["metric"])

print(

    "RAFFICA API:",

    obs["metric"].get("windGust")

)

# =========================

# LEGGE LA RAFFICA

# =========================

raffica_kmh = obs["metric"].get("windGust")

if raffica_kmh is None:

    raise Exception("Raffica vento non disponibile")

print(f"Raffica rilevata: {raffica_kmh:.1f} km/h")

# =========================

# VENTO SOPRA LA SOGLIA

# =========================

if raffica_kmh >= SOGLIA:

    if not stato["allarme_attivo"]:

        messaggio = (

            "🌬️ ALLERTA VENTO VEVOR\n\n"

            f"Raffica: {raffica_kmh:.1f} km/h\n"

            f"Soglia: {SOGLIA} km/h"

        )

        send_url = (

            f"https://api.telegram.org/"

            f"bot{TELEGRAM_TOKEN}/sendMessage"

        )

        telegram_response = requests.post(

            send_url,

            json={

                "chat_id": CHAT_ID,

                "text": messaggio

            },

            timeout=20

        )

        print(

            "RISPOSTA TELEGRAM:",

            telegram_response.text

        )

        telegram_response.raise_for_status()

        print("🔔 Notifica Telegram inviata.")

        stato["allarme_attivo"] = True

    else:

        print(

            "Vento ancora sopra la soglia: "

            "nessuna nuova notifica."

        )

# =========================

# VENTO SOTTO LA SOGLIA

# =========================

else:

    if stato["allarme_attivo"]:

        print(

            "Vento tornato sotto la soglia: "

            "sistema riarmato."

        )

    stato["allarme_attivo"] = False

# =========================

# SALVA LO STATO

# =========================

with open(STATE_FILE, "w") as f:

    json.dump(stato, f)

print("STATO SALVATO:", stato)

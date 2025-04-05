import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(site):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"🚨 Site fora do ar: {site}"}
    requests.post(url, data=data)

def check_site(site):
    try:
        response = requests.get(site, timeout=5)
        return response.status_code == 200
    except:
        return False

with open("sites.txt") as f:
    sites = [line.strip() for line in f]

for site in sites:
    if not check_site(site):
        send_telegram_alert(site)

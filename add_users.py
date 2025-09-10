print("🚀 Script lancé...")

from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
import time
from dotenv import load_dotenv
import os

# Charger les variables du fichier .env
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")


client = TelegramClient('session_name', api_id, api_hash)
client.start(phone)

channel = client.get_entity(channel_username)

# Charger les utilisateurs depuis users.csv
users = []
with open('users.csv', 'r') as f:
    for line in f:
        username_or_id = line.strip()
        if username_or_id:
            users.append(username_or_id)

print(f"{len(users)} utilisateurs à ajouter.")

for user in users:
    try:
        client(InviteToChannelRequest(channel, [user]))
        print(f"✅ Utilisateur ajouté : {user}")
    except Exception as e:
        print(f"❌ Erreur pour {user}: {e}")
    time.sleep(delay)

client.disconnect()
print("✅ Script terminé.")
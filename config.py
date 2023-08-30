import os

API_ID = int(os.environ.get("API_ID", '25947375'))
API_HASH = os.environ.get("API_HASH", 'af7b9b8a0d377b4d3735199e9df008af')
BOT_TOKEN = os.environ.get("BOT_TOKEN", '6331021246:AAF9a2NzaPBpG3ZvP7BvfelDJuA7SlkunYY')
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("6408116706"))
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '-1001629572693')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)

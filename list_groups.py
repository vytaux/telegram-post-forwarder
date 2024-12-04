import configparser
from telethon import TelegramClient

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

API_ID = int(config['TELEGRAM']['API_ID'])
API_HASH = config['TELEGRAM']['API_HASH']
PHONE_NUMBER = config['TELEGRAM']['PHONE_NUMBER']

client = TelegramClient('session/list_groups', API_ID, API_HASH)
# Required for login
client.start(phone=PHONE_NUMBER)

async def main():
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            print(f"Group Name: {dialog.name}, ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
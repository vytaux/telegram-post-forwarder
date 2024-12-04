import configparser
from telethon import TelegramClient, events, types

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

API_ID = int(config['TELEGRAM']['API_ID'])
API_HASH = config['TELEGRAM']['API_HASH']
PHONE_NUMBER = config['TELEGRAM']['PHONE_NUMBER']

USER_ID_TO_FORWARD = int(config['GROUPS']['USER_ID_TO_FORWARD'])
TARGET_GROUP_ID = int(config['GROUPS']['TARGET_GROUP_ID'])
ORIGINAL_GROUP_ID = int(config['GROUPS']['ORIGINAL_GROUP_ID'])

# Create the Telegram client
client = TelegramClient('session/main', API_ID, API_HASH)
# Required for login
client.start(phone=PHONE_NUMBER)

@client.on(events.NewMessage(chats=ORIGINAL_GROUP_ID))
async def forward_message(event):
    # Forward messages posted by the channel or group itself that contain specific text
    if event.message.from_id is None and isinstance(event.message.peer_id, types.PeerChannel):
        if 'Instagram by clicking' in event.message.message:
            # Forward the message to the target group
            await client.forward_messages(TARGET_GROUP_ID, event.message)

async def main():
    print(f"Listening for admin/channel messages in group {ORIGINAL_GROUP_ID}...")
    # Keep the script running
    await client.run_until_disconnected()

# Start the client and run the event loop
with client:
    client.loop.run_until_complete(main())
from telethon import TelegramClient, events
import os

# Your API ID and Hash
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')

# Create the client and start the bot
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
  """Handles incoming messages."""
  if event.message.message.lower() == '/start':
    await event.respond('Hello! I am a simple Telegram bot running on Koyeb.')
  else:
    await event.respond('You said: ' + event.message.message)

# Keep the bot running
print("Bot started")
client.run_until_disconnected()

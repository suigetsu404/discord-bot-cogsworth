import asyncio
import sqlite3
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

# token import
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    raise ValueError('DISCORD_TOKEN environment variable is not set')
GEMINI_API_KEY = os.getenv("GEMINI_TOKEN")
if not GEMINI_API_KEY:
    raise ValueError('GEMINI_TOKEN environment variable is not set')
genai.configure(api_key=GEMINI_API_KEY)

# intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

# launcher
async def main():
    connection = sqlite3.connect("bot.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS karma
            (
                user_id INTEGER PRIMARY KEY,
                points INTEGER DEFAULT 0
        )
    """)
    connection.commit()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reminders
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                channel_id INTEGER,
                remind_time TIMESTAMP,
                message TEXT
        )
    """)
    connection.commit()
    connection.close()
    print("Successfully connected to bot.db.")
    initial_extensions = [
        'cogs.fun',
        'cogs.api',
        'cogs.moderation',
        'cogs.memory',
        'cogs.misc',
        'cogs.listeners'
    ]
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f"Successfully loaded extension: {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}: {e}")
    print("Successfully loaded all extensions.")
    print("Bot is starting...")
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())


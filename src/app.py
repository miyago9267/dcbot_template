import discord
import asyncio, time, random, os, re

from models.bot import Bot
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix=os.getenv('COMMAND_PREFIX'), intents=intents)

def bot_start():
    bot.setup(os.getenv('BOT_TOKEN'))

if __name__=='__main__':
    bot_start()
import discord
import discord.emoji
import asyncio, time, random, os, re

from models.kokoro import Kkr
from models.bot import Bot
from models.botManager import initialize_manager, KkrManager
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = Bot(command_prefix=os.getenv('COMMAND_PREFIX'), intents=intents)
kokoro = Kkr(bot)

def bot_start():
    bot.setup()

if __name__=='__main__':
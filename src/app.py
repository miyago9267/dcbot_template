import discord
import os
from models.bot import Bot
from dotenv import load_dotenv

load_dotenv()

def bot_start():
    bot = Bot()
    bot.setup(os.getenv('BOT_TOKEN'))

if __name__=='__main__':
    bot_start()
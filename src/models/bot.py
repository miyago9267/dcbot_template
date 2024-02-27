import discord.ext.commands as commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix=os.getenv('COMMAND_PREFIX'),
            intents=intents
        )

    def setup_hook(self, token):
        self.start(token)

    async def on_ready(self):
        await self.add_cog(BotEventsCog(self))
        # await self.add_cog(BotCommandsCog(self))

class BotEventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready!')
        print('Name: {}'.format(self.bot.user.name))
        print('ID: {}'.format(self.bot.user.id))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')
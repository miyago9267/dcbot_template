from dotenv import load_dotenv
import discord.ext.commands as commands

load_dotenv()

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, token):
        self.run(token)

    async def on_ready(self):
        await self.add_cog(BotEventsCog(self))

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
from discord.ext import commands

class BOT_NAME(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content.startswith('!ping'):
            await message.channel.send('pong')
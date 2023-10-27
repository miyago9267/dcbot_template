import discord
import discord.emoji
import json

class Kkr(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, bot):
        if not hasattr(self, 'initialized'):
            self.bot = bot
            self.initialized = True
        self.server = -1
        self.channel = -1
        self.mode = "Off"
        self.channelName = "Not set yet"
        self.serverName = "Not set yet"

    async def setServer(self, server, msg):
        self.server = int(server)
        self.serverName = self.bot.get_server(int(server)).name
        await msg.channel.send(
            f"Server has been set to {self.serverName}" 
        )

    async def setChannel(self, channel, msg):
        self.channel = int(channel)
        self.channelName = self.bot.get_channel(int(channel)).name
        await msg.channel.send(
            f"Channel has been set to {self.channelName}"
        )

    async def setMode(self, mode, msg):
        self.mode = mode
        await msg.channel.send(
            f"Mode has been set to {self.mode}"
        )

    async def getStatus(self, owo, msg):
        embed = discord.Embed(
            title = "Owner Command Status",
            description = "**How can i do for u**\n\n"
        )
        embed.add_field(name="Server: ", value=self.serverName, inline=False)
        embed.add_field(name="Channel: ", value=self.channelName, inline=False)
        embed.add_field(name="Mode: ", value=self.mode, inline=False)
        await msg.channel.send(embed=embed)

    async def setOff(self, owo, msg):
        self.mode = "Off"
        await self.setMode()

    async def send(self, mes, msg):
        channel = self.bot.get_channel(self.channel)
        if self.mode == "Off":
            await msg.channel.send("The bot is currently off")
        else:
            await channel.send(mes)
            await msg.channel.send(f"Message sent to {self.channelName}!")


    async def command(self, cmd, msg):
        cmdList = {
            "send": self.send,
            "status": self.getStatus,
            "mode": self.setMode,
            "server": self.setServer,
            "channel": self.setChannel,
            "off": self.setOff
        }
        
        await cmdList.get(cmd.split(" ")[0],
            lambda msg: msg.channel.send("Command not found"))(" ".join(cmd.split(" ")[1:]), msg)
        

    async def sending_test(self, msg):
        print(self.bot)
        channel_id = 1011672939504087055
        channel = self.bot.get_channel(channel_id)
        await channel.send(msg)

    @classmethod
    def get_instance(cls):
        return cls._instance
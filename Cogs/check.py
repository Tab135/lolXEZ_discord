import discord
import random
from discord.ext import commands
key = []

class cock(commands.Cog):
    def __init__(self, bot):
        self.client = bot
    @commands.Cog.listener()
    async def on_message(sef, message):
     for i in range(len(key)):
        if key[i] in message.content:
            await message.channel.send()


def setup(bot):
    bot.add_cog(cock(bot))

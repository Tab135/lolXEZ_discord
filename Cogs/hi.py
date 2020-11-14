import discord
from discord.ext import commands

class Ex(commands.Cog):
    def __init__(self, bots):
        self.client = bots




def setup(bot):
    bot.add_cog(Ex(bot))

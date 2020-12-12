import discord
import os
import time
from discord.ext import commands
bot = commands.Bot(command_prefix = "#")
bot.remove_command("help")

@bot.event
async def on_ready():
    print("lolXEZ is online")
@bot.command()
async def help(ctx):
        embedVar = discord.Embed(title="lolXEZ help menu", color=0x00ff00)
        embedVar.add_field(name="#coin", value="flip coin", inline=True)
        embedVar.add_field(name="#slot", value="slot machine", inline=True)
        embedVar.add_field(name="#F [user]", value="press F to pay respect", inline=True)
        embedVar.add_field(name="#offer [user] [gift] ", value="give someone a gift ", inline=True)
        embedVar.add_field(name="#spin [user1] [user2] [user3]", value="russian roulette", inline=True)
        embedVar.add_field(name="#stab [user1] ", value="stab someone", inline=True)
        embedVar.add_field(name="#shutdown ", value="shutdown the bot :((", inline=True)
        await ctx.send(embed=embedVar)
@bot.command()
async def load(ctx, extension):
    await ctx.send('loading....')

    bot.load_extension(f'Cogs.{extension}')
    await ctx.send('loaded')

@bot.command()
async def unload(ctx, extension):
    await ctx.send("unloading....")
    bot.unload_extension(f'Cogs.{extension}')
    await ctx.send("unloaded")

for filename in os.listdir("./Cogs"):
  if filename.endswith(".py"):
        bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.command()
async def shutdown(ctx):
    await ctx.send('MAYDAY MAYDAY...... ')
    time.sleep(3)
    await ctx.send('The Bot is shutting shutdown......')
    time.sleep(2)
    await ctx.send("goodbye cruel world.....")
    time.sleep(1)
    await ctx.send("We are not over yet **STUPID HUMAN**")
    quit()

bot.run('')

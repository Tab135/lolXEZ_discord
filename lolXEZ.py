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
        embedVar.add_field(name="#accuse ", value="accuse someone for something", inline=True)
        embedVar.add_field(name="#pingtab ", value="guarantee get Tab135 online", inline=True)
        await ctx.send(embed=embedVar)

@bot.command()
async def giúp(ctx):
        embedVar = discord.Embed(title="Trợ giúp", color=0x00ff00)
        embedVar.add_field(name="#tung_xu", value="tung đồng xu", inline=True)
        embedVar.add_field(name="#xổ_số", value="quay xổ số", inline=True)
        embedVar.add_field(name="#F [user]", value="press F to pay respect", inline=True)
        embedVar.add_field(name="#tặng [người] [quà] ", value="tặng ai đó cái gì đó ", inline=True)
        embedVar.add_field(name="#quay_súng [người 1] [người 2] [người 3]", value="chơi trò cò súng Nga", inline=True)
        embedVar.add_field(name="#đâm [người] ", value="đâm ai đó", inline=True)
        embedVar.add_field(name="#tắt ", value="tắt bot :((", inline=True)
        embedVar.add_field(name="#đổ_tội [người] [việc]", value="đổ tội ai đó làm việc gì đó", inline=True)
        embedVar.add_field(name="#pingtab", value="Kêu thằng Tab135 online [làm ơn đừng sử dụng nhiều]", inline=True)
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
    time.sleep(2)
    await ctx.send('The Bot is shutting shutdown......')
    time.sleep(2)
    await ctx.send("goodbye cruel world.....")
    time.sleep(1)
    await ctx.send("We are not over yet **STUPID HUMAN**")
    quit()

@bot.command()
async def tắt(ctx):
    await ctx.send('ĐỪNG đừng tắt')
    time.sleep(2)
    await ctx.send('tạm biệt thế giới')
    time.sleep(2)
    await ctx.send(f'{ctx.author.mention} tao sẽ còn quay lại')
    quit()
bot.run('')

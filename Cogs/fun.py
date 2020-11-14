import discord
import random
from discord.ext import commands


class Ex(commands.Cog):
    def __init__(self, bot):
        self.client = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun is loaded')

    @commands.command()
    async def slot(self, ctx):

        emojis = ['🍎', '🍊', '🍐' ,'🍋', '🍉', '🍇']
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ | {a} | {b} | {c} |]**"

        if (a == b == c):
            embedVar = discord.Embed(title="-----SLOT------", color=0xf1c40f)
            embedVar.add_field(name=f"{slotmachine}", value=f"{ctx.author.mention} All matching, you won! ")
            await ctx.send(embed=embedVar)

        elif (a == b) or (a == c) or (b == c):
            embedVar = discord.Embed(title="-----SLOT------", color=0xe74c3c)
            embedVar.add_field(name=f"{slotmachine}", value=f"{ctx.author.mention} 2 in a row, you won!")
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title="-----SLOT------", color=0x3498db)
            embedVar.add_field(name=f"{slotmachine}", value=f"{ctx.author.mention} No match, you lost 😢")
            await ctx.send(embed=embedVar)
    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        coinsides = ['Heads', 'Tails','oof the coin has droped']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")
    @commands.command()
    async def spin(self,ctx,user1,user2,user3):
        chamber = random.randint(1,2)

        if chamber == 1:
            await ctx.send(f'**{user1}** was unlucky and got shot')
            await ctx.send(f'**{user2}** was a lucky asshole')
            await ctx.send(f'**{user3}** was a lucky asshole')
            return
        else:
            await ctx.send(f'**{user1}** was a lucky asshole')
        chamber = random.randint(1,2)
        if chamber == 1:
            await ctx.send(f'**{user2}** was unlucky and got shot')
            await ctx.send(f'**{user3}** was a lucky asshole')
        else:
            await ctx.send(f'**{user2}** was a lucky asshole')
            await ctx.send(f'**{user3}** was unlucky and got shot')




def setup(bot):
    bot.add_cog(Ex(bot))
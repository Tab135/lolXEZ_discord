import discord
import random
from discord.ext import commands


class homie(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('homie is loaded')

    @commands.command()
    async def offer(self, ctx, member, gift, part2: commands.clean_content = None,part3: commands.clean_content = None ):
     gift2 = f"**{part2}** " if part2 else ""
     gift3 = f"**{part3}** " if part3 else ""
     await ctx.send(f"**{ctx.author.name}** has given **{member}** a **{gift}** {gift2} {gift3} ")

    @commands.command()
    async def F(self, ctx, *, text: commands.clean_content = None):
        hearts = ['❤', '💛', '💚', '💙', '💜']
        reason = f"to **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")
    @commands.command()
    async def stab(self,ctx,user):
        respone = [f'Holy Shit **{ctx.author.name}** has stabbed **{user}** ',
                   f' **{user}** pulled uno reverse card on  **{ctx.author.name}** ',
                   f'lol **{ctx.author.name}** accidentally stabbed themself']
        await ctx.send(random.choice(respone))


def setup(bot):
    bot.add_cog(homie(bot))
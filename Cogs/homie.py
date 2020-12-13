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
    async def F(self, ctx, *, user):
        hearts = ['❤', '💛', '💚', '💙', '💜']

        await ctx.send(f"**{ctx.author.name}** has paid their respect to {user}{random.choice(hearts)}")
    @commands.command()
    async def stab(self,ctx,user):
        respone = [f'Holy Shit **{ctx.author.name}** has stabbed **{user}** ',
                   f' **{user}** pulled uno reverse card on  **{ctx.author.name}** ',
                   f'lol **{ctx.author.name}** accidentally stabbed themself',
                   f'Damn **{user}** is dead ']
        await ctx.send(random.choice(respone))
    @commands.command()
    async def blame(self,ctx,user,something,something2: commands.clean_content = None,something3: commands.clean_content = None,something4: commands.clean_content = None,something5: commands.clean_content = None,something6: commands.clean_content = None):
        smt2 = something2 if something2 else ""
        smt3 = something3 if something3 else ""
        smt4 = something4 if something4 else ""
        smt5 = something5 if something5 else ""
        smt6 = something6 if something6 else ""
        await ctx.message.delete()
        await ctx.send(f"Hmmm someone accused {user} of {something} {smt2} {smt3} {smt4} {smt5} {smt6} ")


def setup(bot):
    bot.add_cog(homie(bot))

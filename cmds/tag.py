import discord
from discord.ext import commands
from core.classes import cog_Extention

class tag(cog_Extention):

    @commands.command()
    async def QQ(self,ctx):
        await ctx.send('是在哭是吧')
    
    @commands.command()
    async def AA(self,ctx):
        await ctx.send('是在是吧')


def setup(bot):
    bot.add_cog(tag(bot))
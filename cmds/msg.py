import discord
from discord.ext import commands
from core.classes import cog_Extention

class msg(cog_Extention):

    @commands.Cog.listener()
    async def on_message(self, mmm):
        if mmm.content == '哭阿':
            await mmm.channel.send('嫩拉')

def setup(bot):
    bot.add_cog(msg(bot))
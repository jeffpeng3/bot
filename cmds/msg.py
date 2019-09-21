import discord
from discord.ext import commands
from core.classes import cog_Extention

class msg(cog_Extention):

    @commands.Cog.listener()
    async def on_message(self, mmm):
        key = ['哭阿','哭啊']
        if mmm.content in key:
            await mmm.channel.send('嫩拉')

def setup(bot):
    bot.add_cog(msg(bot))
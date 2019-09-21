import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(">> bot is online <<")

                   
bot.run('NjI0NjMxMjc5NDEzMTAwNTc0.XYT6UA.eTPOGoRm2u0j7PgJJrClDgmT8LI')
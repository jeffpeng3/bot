import discord
from discord.ext import commands
import json

with open('Setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.command()
async def QQ(ctx):
    await ctx.send('是在哭是吧')
                   
bot.run(jdata['token'])
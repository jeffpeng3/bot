import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'load {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unload {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reload {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run('NjI0NjMxMjc5NDEzMTAwNTc0.XYZD8A.tyKWGYHSNQbvUnowl5gjeTq4Opo')
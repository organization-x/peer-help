import discord
from discord.ext import commands

from discord import client

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    await ctx.send(embed=embed)                

bot.run('MTAyNTY0MjgzMTU5NzAyMzI0Mg.G7Ym7Q.-Bf_RaVhGoPZyjrzDP1qXWRIWOQ83Wqz-Otvy8')
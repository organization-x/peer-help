from ast import Delete
import discord
from discord.ext import commands
import os
from model import asyncio
from model import main
from asyncio import sleep
import time



intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#output = asyncio.run(main('https://www.notion.so/IncSkill-Website-Product-Spec-673589270f7241dda9cb27fecab8af10%27'))

@bot.command()
async def ping(ctx):
    output = await main('https://www.notion.so/IncSkill-Website-Product-Spec-673589270f7241dda9cb27fecab8af10%27')
    asyncio.run(main('https://www.notion.so/IncSkill-Website-Product-Spec-673589270f7241dda9cb27fecab8af10%27'))
    await ctx.send(output)

@bot.command()
async def peer(ctx):
    peer=discord.Embed(title="PEER is Reviewing your Product Spec", url="", description="", color=0xffffff)
    peer.set_image(url="https://gifimage.net/wp-content/uploads/2017/10/cool-loading-animation-gif-2.gif")
    em = discord.Embed(title="YOU NEED TO SET A TITLE")

    #embed=discord.Embed(title="This is a Test", url="", description="hello everyone", color=0x313435)
    await ctx.send(embed=peer, delete_after=7)
    await asyncio.sleep(7)
    await ctx.send(embed=em)

bot.run('TOKEN')

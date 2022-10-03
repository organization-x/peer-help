import discord
import model
import nest_asyncio
import asyncio
from notion_extraction import extract_product_spec_text, parse_product_spec_text, extract_id_from_url
import requests
import aiohttp 
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
    loop = asyncio.get_event_loop()
    feedback = loop.run_until_complete(model.main('https://www.notion.so/IncSkill-Website-Product-Spec-673589270f7241dda9cb27fecab8af10'))
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description= feedback, color=0xFF5733)
    await ctx.send(embed=embed)                

bot.run('TOKEN')

#Importing libraries, these are all we need
from tkinter import Button
import discord
from discord.ext import commands
import os
from model import main
import Paginator
 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)

@bot.command()
async def pages(ctx):
    embeds = [discord.Embed(title="First embed"),
          discord.Embed(title="Second embed"),
          discord.Embed(title="Third embed")]
    
    await Paginator.Simple().start(ctx, pages=embeds)


bot.run(os.environ['product_spec_bot'])
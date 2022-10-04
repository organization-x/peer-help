import discord
from discord.ext import commands
import os
from model import asyncio
from model import main
 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)
 
#output = asyncio.run(main('https://www.notion.so/IncSkill-Website-Product-Spec-673589270f7241dda9cb27fecab8af10'))
 
@bot.command()
async def ping(ctx):
   output = await main('https://www.notion.so/IncSkill-Website-Product-Spec-673589270f7241dda9cb27fecab8af10')
   await ctx.send(output)
 
@bot.command()
async def score(ctx, arg):
   output = await main(arg)
   embed=discord.Embed(title="Product Spec Review", url="https://github.com/organization-x/peer-help", description=output, color=3447003)
   await ctx.send(embed=embed)   
          
token = os.environ['product_spec_bot']
bot.run(token)



              




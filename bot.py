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

@bot.command()
async def peer(ctx, arg):
   
   peer = discord.Embed(title="PEER is Reviewing your Product Spec!", url="https://github.com/organization-x/peer-help", description="", color=3447003)
   peer.set_image(url="https://cdn.dribbble.com/users/980063/screenshots/2460821/square-shape-morph2.gif")

# https://cdn.dribbble.com/users/980063/screenshots/2460821/square-shape-morph2.gif
# https://gt3themes.com/wp-content/uploads/2016/02/loading.gif
# https://gifimage.net/wp-content/uploads/2017/10/cool-loading-animation-gif-2.gif
# https://media.tenor.com/IpY-rwdLcnQAAAAC/infinite.gif
   

   await ctx.send(embed=peer, delete_after=7)
   output = await main(arg)
   newEmbed = discord.Embed(title="Product Spec Review", description=output, color=3447003)
   
   await ctx.send(embed=newEmbed)

# NEEDS WORK


bot.run(os.environ['product_spec_bot'])

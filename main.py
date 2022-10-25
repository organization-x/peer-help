import discord
from discord.ext import commands
import os
from model import main
 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)
 
@bot.command()
async def peer(ctx, arg):
   peer = discord.Embed(title="PEER is Reviewing your Product Spec!", url="https://github.com/organization-x/peer-help", description="", color=3447003)
   peer.set_image(url="https://cdn.dribbble.com/users/980063/screenshots/2460821/square-shape-morph2.gif")

   await ctx.send(embed=peer, delete_after=7)

   output = main(arg)
   newEmbed = discord.Embed(title="Product Spec Review", description=output, color=3447003)
   
   await ctx.send(embed=newEmbed)

bot.run(os.environ['BOT_TOKEN'])

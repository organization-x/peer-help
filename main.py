import discord
from discord.ext import commands
import os
from model import main
import Paginator

 
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='#', intents=intents)


@bot.command()
async def peer(ctx, arg):
   peer = discord.Embed(title="PEER is Reviewing your Product Spec!", url="https://github.com/organization-x/peer-help", description="", color=3447003)
   peer.set_image(url="https://cdn.dribbble.com/users/1148781/screenshots/3233207/media/3255674065b3b19a7f4227cd6e3be153.gif")

   await ctx.send(embed=peer, delete_after=7)
   output = await main(arg)
   
   newEmbed = discord.Embed(title="Product Spec Review", description=output, color=3447003)
   
   await ctx.send(embed=newEmbed)

@bot.command()
async def pages(ctx, arg):
   
   embeds = []
   output = await main(arg)
   
   number = 0
   for i in range(len(output)):
      embeds.append(discord.Embed(title=f"Embed #{(i + 1)}", description=output[number]))
      number+=1
   
   await Paginator.Simple().start(ctx, pages=embeds)

bot.run(os.environ['product_spec_bot'])

# https://cdn.dribbble.com/users/1148781/screenshots/3233207/media/3255674065b3b19a7f4227cd6e3be153.gif
# https://cdn.dribbble.com/users/980063/screenshots/2460821/square-shape-morph2.gif

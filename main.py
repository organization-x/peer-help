import discord
from discord.ext import commands
import os
import Paginator
from model import main
 
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
 
@bot.command()
async def peer(ctx, arg):

   if ctx.channel.name in ['tech-team', 'bot_testing']:
      peer = discord.Embed(title="PEER is Reviewing your Product Spec!", url="https://github.com/organization-x/peer-help", description="", color=3447003)
      peer.set_image(url="https://cdn.dribbble.com/users/980063/screenshots/2460821/square-shape-morph2.gif")

      await ctx.send(embed=peer, delete_after=0)

      output = main(arg)
      new_embed = discord.Embed(title="Product Spec Review", description=output, color=3447003)

      embeds = []

      for i, j in output.items():
         embeds.append(discord.Embed(title=f"{i}", description=output[i], color=3447003))
      
      return await Paginator.Simple().start(ctx, pages=embeds)

   output = 'Currently, PEER is only available to AI Camp Team members. Sorry for the inconvenience. If you are an AI Camp Team member, please use PEER in the Tech Team channel.'
   new_embed = discord.Embed(title="Not The Right Channel!", description=output, color=3447003)
   return await ctx.send(embed=new_embed)

bot.run(os.environ['BOT_TOKEN'])

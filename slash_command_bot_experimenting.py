import discord
from discord import app_commands
import os

token = os.environ['product_spec_bot']
intents = discord.Intents.default()
intents.message_content = True

class aclient(discord.Client) :
    def _init__(self):
        super(). init_(intents=discord.Intents.default())
        self. synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        # if not self.synced:
        #     await tree.sync(guild = discord.Object(id = 1019793646171734056))
        #     self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "test", description = "testing", guild = discord.Object(id = 1019793646171734056))
async def self (interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello {name}! I was made with Discord.py!", ephemeral = True)
client.run(token)
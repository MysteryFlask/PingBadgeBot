import discord
from discord import app_commands

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "ping", description = "Pong", guild=discord.Object(id=111111111111111111)) # Replace with your guild id (see README.md)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=111111111111111111))  # See above
    print("Ready!")

client.run("TOKEN") # Replace this with your Discord bot token (see README.md)

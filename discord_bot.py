import discord
import dotenv
from discord.ext import commands
import os
import asyncio
import random
import json
from colorama import Fore, Back, Style
from discord import app_commands, utils
from discord.ext import commands, tasks
from itertools import cycle

dotenv.load_dotenv()
discord_token = os.getenv('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())
client.remove_command('help')

alicelogs = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░███░░░░░██░░░░░░░░████░░░██████░░░████████░░██░░░░░░░░░███████░░░░██████░░░░░██████░░
░░░░██ ██░░░ ██░░░░░░░░ ██░░░██░░░ ██░ ██░░░░░░░ ██░░░░░░░░██░░░░ ██░░██░░░ ██░░░██░░░ ██░
░░░██░░ ██░░ ██░░░░░░░░ ██░░ ██░░░░░░░ ██░░░░░░░ ██░░░░░░░ ██░░░░ ██░ ██░░░░░░░░ ██░░░░░░░
░░██░░░░ ██░ ██░░░░░░░░ ██░░ ██░░░░░░░ ██████░░░ ██░░░░░░░ ██░░░░ ██░ ██░░░████░░ ██████░░
░ █████████░ ██░░░░░░░░ ██░░ ██░░░░░░░ ██░░░░░░░ ██░░░░░░░ ██░░░░ ██░ ██░░░ ██░░░░░░░░ ██░
░ ██░░░░ ██░ ██░░░░░░░░ ██░░ ██░░░ ██░ ██░░░░░░░ ██░░░░░░░ ██░░░░ ██░ ██░░░ ██░░░██░░░ ██░
░ ██░░░░ ██░ ████████░░████░░ ██████░░ ████████░ ████████░░ ███████░░░ ██████░░░░ ██████░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
#  v0.1.2  #  By: WaterMeloDev  #
#################################
"""

@client.event
async def on_ready():
    try: 
        synced = await client.tree.sync()
        print(f"{Fore.GREEN}Synced {len(synced)} commands!{Fore.RESET}")
    except:
        print(f'{Fore.RED}already synced{Fore.RESET}')
    change_status.start()
    print(f"{Fore.GREEN}Loading a connection with {client.user}{Fore.RESET}")
    await asyncio.sleep(3)
    print(f"{Fore.GREEN}Connected!{Fore.RESET}")
    print(f"{Fore.GREEN}{alicelogs}{Fore.RESET}")
async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f"{len(client.guilds)} guilds!", url="https://www.twitch.tv/alicelogs"))

# help command
@client.tree.command(name='help', description='Shows this message')
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Help", description="Here are all the commands you can use with me!", color=0x00ff00)
    embed.add_field(name="!help", value="Shows this message", inline=False)
    embed.add_field(name="!hide", value="Hides your username from the logs", inline=False)
    embed.add_field(name="!unhide", value="Unhides your username from the logs", inline=False)
    embed.add_field(name="!support", value="Shows ways to support the bot", inline=False)

    await interaction.response.send_message(embed=embed, ephemeral=True)

# support command
@client.tree.command(name='support', description='Shows ways to support the bot')
async def support(interaction: discord.Interaction):
    embed = discord.Embed(title="Support", color=0xFFFFFF)
    embed.add_field(name="Infomation", value="I monitor your server on Twitch ;>", inline=False)
    embed.add_field(name="Support", value="https://discord.gg/6dCMQt33aw", inline=False)
    embed.add_field(name="Vote for me!", value="[Vote](https://universe-list.xyz/bots/1131451736247255091)", inline=False)
    embed.add_field(name="Invite me!", value="[Invite](https://discord.com/api/oauth2/authorize?client_id=1131451736247255091&permissions=2611341028544&scope=bot)", inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)

# hide command
@client.tree.command(name='hide', description='Hides your username from the logs')
async def hide(interaction: discord.Interaction):
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    if interaction.user.name in users['hidden']:
        await interaction.response.send_message("You are already hidden!", ephemeral=True)
    else:
        users['hidden'].append(interaction.user.name)
        with open('data/users.json', 'w') as f:
            json.dump(users, f)
        await interaction.response.send_message("You are now hidden!", ephemeral=True)

# unhide command
@client.tree.command(name='unhide', description='Unhides your username from the logs')
async def unhide(interaction: discord.Interaction):
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    if interaction.user.name in users['hidden']:
        users['hidden'].remove(interaction.user.name)
        with open('data/users.json', 'w') as f:
            json.dump(users, f)
        await interaction.response.send_message("You are now unhidden!", ephemeral=True)
    else:
        await interaction.response.send_message("You are already unhidden!", ephemeral=True)

# setup command
@client.tree.command(name='setup', description='Sets up the bot')
async def setup(interaction: discord.Interaction):
    # open guilds.json
        with open('data/guilds.json', 'r') as f:
            guilds = json.load(f)
        # if guild is already setup
        if str(interaction.guild.id) in guilds['guilds']:
            embed = discord.Embed(title="Error", description="This guild is already setup!", color=0xFF0000)
            await interaction.response.send_message(embed=embed)
        # if guild is not setup
        else:
            # add guild to guilds
            guilds['guilds'].append(interaction.guild.id)
            # write to guilds.json
            with open('data/guilds.json', 'w') as f:
                json.dump(guilds, f, indent=4)
            embed = discord.Embed(title="Success", description="This guild is now setup and will appear in logs.", color=0x00FF00)
            await interaction.response.send_message(embed=embed)
            print(f"{interaction.guild.name} is now setup")

async def main():
    async with client:
        try:
            await load()
        except Exception as e:
            print(f"{Fore.RED}Error loading cogs: {e}")
        await client.start(discord_token)

asyncio.run(main())

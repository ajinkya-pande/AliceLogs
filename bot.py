import discord
import dotenv
from discord.ext import commands
import os
import asyncio
import random

from colorama import Fore, Back, Style
from discord import app_commands, utils
from discord.ext import commands, tasks
from itertools import cycle

dotenv.load_dotenv()
token = os.getenv('TOKEN')

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
@client.tree.command(name="help", description="get help")
async def help_cmd(interaction: discord.Interaction):
    embed = discord.Embed(title="Help", color=0xFFFFFF)
    embed.add_field(name="Infomation", value="I monitor your server on Twitch ;>.", inline=False)
    embed.add_field(name="Support", value="https://discord.gg/6dCMQt33aw", inline=False)
    embed.add_field(name="Vote for me!", value="[Vote](https://universe-list.xyz/bots/1131451736247255091)", inline=False)
    embed.add_field(name="Invite me!", value="[Invite](https://discord.com/api/oauth2/authorize?client_id=1131451736247255091&permissions=2611341028544&scope=bot)", inline=False)
    await interaction.response.send_message(embed=embed)

async def main():
    async with client:
        try:
            await load()
        except Exception as e:
            print(f"{Fore.RED}Error loading cogs: {e}")
        await client.start(token)

asyncio.run(main())
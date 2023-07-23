import discord
import json
from discord.ext import commands

class CMDs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"cmd cog loaded")

    # hide command
    # replaces your name in logs with "Hidden"
    @commands.command(name="hide", description="hide your name in logs")
    async def hide_cmd(self, ctx):
        # open users.json
        with open('data/users.json', 'r') as f:
            users = json.load(f)
        # if user is already hidden
        if ctx.author.name in users['hidden']:
            embed = discord.Embed(title="Error", description="You are already hidden!", color=0xFF0000)
            await ctx.send(embed=embed)
        # if user is not hidden
        else:
            # add user to hidden
            users['hidden'].append(ctx.author.name)
            # write to users.json
            with open('data/users.json', 'w') as f:
                json.dump(users, f, indent=4)
            embed = discord.Embed(title="Success", description="You are now hidden!", color=0x00FF00)
            await ctx.send(embed=embed)

    # unhide command
    # replaces your name in logs with your name
    @commands.command(name="unhide", description="unhide your name in logs")
    async def unhide_cmd(self, ctx):
        # open users.json
        with open('data/users.json', 'r') as f:
            users = json.load(f)
        # if user is not hidden
        if ctx.author.name not in users['hidden']:
            embed = discord.Embed(title="Error", description="You are not hidden!", color=0xFF0000)
            await ctx.send(embed=embed)
        # if user is hidden
        else:
            # remove user from hidden
            users['hidden'].remove(ctx.author.name)
            # write to users.json
            with open('data/users.json', 'w') as f:
                json.dump(users, f, indent=4)
            embed = discord.Embed(title="Success", description="You are no longer hidden!", color=0x00FF00)
            await ctx.send(embed=embed)
    
    # setup command
    # sets up the bot
    @commands.command(name="setup", description="setup the bot")
    @commands.has_permissions(administrator=True)
    async def setup_cmd(self, ctx):
        # open guilds.json
        with open('data/guilds.json', 'r') as f:
            guilds = json.load(f)
        # if guild is already setup
        if ctx.guild.id in guilds['guilds']:
            embed = discord.Embed(title="Error", description="This guild is already setup!", color=0xFF0000)
            await ctx.send(embed=embed)
        # if guild is not setup
        else:
            # add guild to guilds
            guilds['guilds'].append(await ctx.guild.fetch(id))
            # write to guilds.json
            with open('data/guilds.json', 'w') as f:
                json.dump(guilds, f, indent=4)
            embed = discord.Embed(title="Success", description="This guild is now setup and will appear in logs.", color=0x00FF00)
            await ctx.send(embed=embed)
            print(f"{ctx.guild.name} is now setup")

async def setup(bot):
    await bot.add_cog(CMDs(bot))

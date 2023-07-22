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
        with open('users.json', 'r') as f:
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
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=4)
            embed = discord.Embed(title="Success", description="You are now hidden!", color=0x00FF00)
            await ctx.send(embed=embed)

    # unhide command
    # replaces your name in logs with your name
    @commands.command(name="unhide", description="unhide your name in logs")
    async def unhide_cmd(self, ctx):
        # open users.json
        with open('users.json', 'r') as f:
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
            with open('users.json', 'w') as f:
                json.dump(users, f, indent=4)
            embed = discord.Embed(title="Success", description="You are no longer hidden!", color=0x00FF00)
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(CMDs(bot))

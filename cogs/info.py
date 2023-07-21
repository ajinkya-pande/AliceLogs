import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"info cog loaded")

    @commands.command(name="help", description="get help")
    async def help_cmd(self, ctx):
        embed = discord.Embed(title="Help", color=0xFFFFFF)
        embed.add_field(name="Infomation", value="I monitor your server on Twitch ;>", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))
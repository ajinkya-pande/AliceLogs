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
        embed.add_field(name="Support", value="https://discord.gg/6dCMQt33aw", inline=False)
        embed.add_field(name="Vote for me!", value="[Vote](https://universe-list.xyz/bots/1131451736247255091)", inline=False)
        embed.add_field(name="Invite me!", value="[Invite](https://discord.com/api/oauth2/authorize?client_id=1131451736247255091&permissions=2611341028544&scope=bot)", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))
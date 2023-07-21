import discord
from discord.ext import commands

class TTS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="tts", description="Send a tts message")
    async def tts(self, ctx, *, message):
        if ctx.author.id == 1119006375868104805:
            await ctx.send(message, tts=True)
        else:
            pass

async def setup(client):
    await client.add_cog(TTS(client))
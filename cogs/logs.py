import discord
import asyncio
from datetime import datetime
import os
from colorama import Fore, Back, Style
from discord.ext import commands

class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Logs cog loaded")
        
    #load bad-words.txt from data folder
    with open("data/bad-words.txt") as file:
        bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        now = datetime.now()
        time = now.strftime("%H:%M")
         # if command has local error handler, return
        if hasattr(ctx.command, 'on_error'):
            return
        
        # get the original exception
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command that does not exist" + Fore.RESET)

        if isinstance(error, commands.MissingPermissions):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command that they do not have permission to use" + Fore.RESET)

        if isinstance(error, commands.MissingRequiredArgument):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command without the required arguments" + Fore.RESET)

        if isinstance(error, commands.BadArgument):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command with a bad argument" + Fore.RESET)

        if isinstance(error, commands.CommandOnCooldown):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command that is on cooldown" + Fore.RESET)

        if isinstance(error, commands.NotOwner):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command that only the owner can use" + Fore.RESET)

        if isinstance(error, commands.MissingRole):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command that requires a role that they do not have" + Fore.RESET)

        if isinstance(error, commands.BotMissingPermissions):
            print(Fore.RED + f"{time} - {ctx.author.name} tried to use a command that the bot does not have permission to use" + Fore.RESET)
        else:
            print(Fore.RED + f"{time} - Error: {error}" + Fore.RESET)
    
    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {ctx.author.name} used a slash command" + Fore.RESET)

    # welcome
    @commands.Cog.listener()
    async def on_member_join(self, member):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {member} has joined a server" + Fore.RESET)
    
    # leave
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {member} has left a server" + Fore.RESET)
    
    # log when the bot joins a server
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - Connecting to new server..." + Fore.RESET)
        await asyncio.sleep(3)
        print(Fore.GREEN + f"{time} - Connected!" + Fore.RESET)

    # log when the bot leaves a server
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - Disconnected from server" + Fore.RESET)

    # log when a message is deleted
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {message.author.name}'s message was deleted" + Fore.RESET)

    # log when a message is edited
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.author.name}'s message was edited" + Fore.RESET)
    
    # log when someone is banned
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {user.name} was banned" + Fore.RESET)

    # log when someone is unbanned
    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {user.name} was unbanned" + Fore.RESET)

    # log when someone is kicked
    @commands.Cog.listener()
    async def on_member_kick(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {user.name} was kicked" + Fore.RESET)

    # log when someone joins a voice channel
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        if before.channel is None:
            print(Fore.GREEN + f"{time} - {member.name} joined {after.channel.name}" + Fore.RESET)
        elif after.channel is None:
            print(Fore.RED + f"{time} - {member.name} left {before.channel.name}" + Fore.RESET)
        else:
            print(Fore.YELLOW + f"{time} - {member.name} moved from {before.channel.name} to {after.channel.name}" + Fore.RESET)

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {user.name} started typing in {channel.name}" + Fore.RESET)

    # log when someone reacts to a message
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {user.name} reacted to a message" + Fore.RESET)

    # log when someone removes a reaction from a message
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {user.name} removed a reaction from a message" + Fore.RESET)

    # log when someone removes all reactions from a message
    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - All reactions were removed from a message" + Fore.RESET)

    # log when someone updates their status
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.name} updated their status" + Fore.RESET)

    # log when someone updates their nickname
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.name} updated their nickname" + Fore.RESET)

    # log when someone updates their role
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.name} updated their role" + Fore.RESET)

    # log when someone updates their activity
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.name} updated their activity" + Fore.RESET)

    # log when someone updates their avatar
    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {before.name} updated their avatar" + Fore.RESET)

    # log when someone updates their username
    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {before.name} updated their username to {after.name}" + Fore.RESET)
    
    # log when channel is created
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {channel.name} was created" + Fore.RESET)

    # log when channel is deleted
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {channel.name} was deleted" + Fore.RESET)

    # log when channel is updated
    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.name} was updated" + Fore.RESET)

    # log when role is created
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {role.name} was created" + Fore.RESET)

    # log when role is deleted
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {role.name} was deleted" + Fore.RESET)

    # log when role is updated
    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.name} was updated" + Fore.RESET)

    # log when emoji is created
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {before.name} was created" + Fore.RESET)

    # log when emoji is deleted
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {before.name} was deleted" + Fore.RESET)

    # log when emoji is updated
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {before.name} was updated" + Fore.RESET)

    @commands.Cog.listener()
    async def on_message(self, message):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {message.author.name} sent a message" + Fore.RESET)

    # log when invite is created
    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {invite.code} was created" + Fore.RESET)

    # log when invite is deleted
    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {invite.code} was deleted" + Fore.RESET)

    # log when webhook is created
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {channel.name} was created" + Fore.RESET)

    # log when webhook is deleted
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {channel.name} was deleted" + Fore.RESET)

    # log when webhook is updated
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {channel.name} was updated" + Fore.RESET)

    # log when integration is created
    @commands.Cog.listener()
    async def on_integration_create(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {integration.name} was created" + Fore.RESET)

    # log when integration is deleted
    @commands.Cog.listener()
    async def on_integration_delete(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {integration.name} was deleted" + Fore.RESET)

    # log when integration is updated
    @commands.Cog.listener()
    async def on_integration_update(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {integration.name} was updated" + Fore.RESET)

    # log when stage instance is created
    @commands.Cog.listener()
    async def on_stage_instance_create(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {stage_instance.name} was created" + Fore.RESET)

    # log when stage instance is deleted
    @commands.Cog.listener()
    async def on_stage_instance_delete(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {stage_instance.name} was deleted" + Fore.RESET)

    # log when stage instance is updated
    @commands.Cog.listener()
    async def on_stage_instance_update(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {stage_instance.name} was updated" + Fore.RESET)

    # log when thread is created
    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {thread.name} was created" + Fore.RESET)

    # log when thread is deleted
    @commands.Cog.listener()
    async def on_thread_delete(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {thread.name} was deleted" + Fore.RESET)

    # log when thread is updated
    @commands.Cog.listener()
    async def on_thread_update(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {thread.name} was updated" + Fore.RESET)

    # log when thread member is created
    @commands.Cog.listener()
    async def on_thread_member_join(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.GREEN + f"{time} - {thread.name} was created" + Fore.RESET)

    # log when thread member is deleted
    @commands.Cog.listener()
    async def on_thread_member_leave(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.RED + f"{time} - {thread.name} was deleted" + Fore.RESET)

    # log when thread member is updated
    @commands.Cog.listener()
    async def on_thread_member_update(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - {thread.name} was updated" + Fore.RESET)

    # log when server name is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server name was updated" + Fore.RESET)

    # log when server icon is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server icon was updated" + Fore.RESET)

    # log when server splash is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server splash was updated" + Fore.RESET)

    # log when server region is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server region was updated" + Fore.RESET)

    # log when server afk channel is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server afk channel was updated" + Fore.RESET)

    # log when server afk timeout is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server afk timeout was updated" + Fore.RESET)

    # log when server verification level is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server verification level was updated" + Fore.RESET)

    # log when server default notifications are updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server default notifications were updated" + Fore.RESET)

    # log when server explicit content filter is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(Fore.YELLOW + f"{time} - Server explicit content filter was updated" + Fore.RESET)

    # log when server vanity url is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        if before.vanity_url_code is None:
            print(Fore.GREEN + f"{time} - Server vanity url was updated" + Fore.RESET)
        elif after.vanity_url_code is None:
            print(Fore.RED + f"{time} - Server vanity url was removed" + Fore.RESET)
        else:
            print(Fore.YELLOW + f"{time} - Server vanity url was updated" + Fore.RESET)

    # log when server description is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        if before.description is None:
            print(Fore.GREEN + f"{time} - Server description was updated" + Fore.RESET)
        elif after.description is None:
            print(Fore.RED + f"{time} - Server description was removed" + Fore.RESET)
        else:
            print(Fore.YELLOW + f"{time} - Server description was updated" + Fore.RESET)

    # log when server banner is updated
    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        if before.banner is None:
            print(Fore.GREEN + f"{time} - Server banner was updated" + Fore.RESET)
        elif after.banner is None:
            print(Fore.RED + f"{time} - Server banner was removed" + Fore.RESET)
        else:
            print(Fore.YELLOW + f"{time} - Server banner was updated" + Fore.RESET)

        

async def setup(client):
    await client.add_cog(Logs(client))
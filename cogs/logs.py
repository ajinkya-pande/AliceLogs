import discord
import re
import asyncio
from datetime import datetime
import os
from colorama import Fore, Back, Style
from discord.ext import commands

def print_event_message(self, time, author_name, message):
        now = datetime.now()
        time = now.strftime("%H:%M")
        lower_author_name = author_name.lower()
        contains_bad_word = any(bad_word in lower_author_name for bad_word in self.bad_words)
        
        if contains_bad_word:
            filtered_author_name = re.sub(r'\b(?:' + '|'.join(map(re.escape, self.bad_words)) + r')\b', '#####', author_name, flags=re.IGNORECASE)
            print(Fore.GREEN + f"{time} - {filtered_author_name} {message}" + Fore.RESET)
        else:
            print(Fore.GREEN + f"{time} - {author_name} {message}" + Fore.RESET)

class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("data/bad-words.txt") as file:
            self.bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Logs cog loaded")


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        now = datetime.now()
        time = now.strftime("%H:%M")
        def print_error_message(ctx, error, error_message):
            now = datetime.now()
            time = now.strftime("%H:%M")
            author_name = ctx.author.name
            lower_author_name = author_name.lower()
            contains_bad_word = any(bad_word in lower_author_name for bad_word in self.bad_words)
            
            if contains_bad_word:
                filtered_author_name = re.sub(r'\b(?:' + '|'.join(map(re.escape, self.bad_words)) + r')\b', '#####', author_name, flags=re.IGNORECASE)
                print(Fore.RED + f"{time} - {filtered_author_name} {error_message}" + Fore.RESET)
            else:
                print(Fore.RED + f"{time} - {author_name} {error_message}" + Fore.RESET)

        if isinstance(error, commands.CommandNotFound):
            print_error_message(ctx, error, "tried to use a command that does not exist")

        elif isinstance(error, commands.MissingPermissions):
            print_error_message(ctx, error, "tried to use a command that they do not have permission to use")

        elif isinstance(error, commands.MissingRequiredArgument):
            print_error_message(ctx, error, "tried to use a command without the required arguments")

        elif isinstance(error, commands.BadArgument):
            print_error_message(ctx, error, "tried to use a command with a bad argument")

        elif isinstance(error, commands.CommandOnCooldown):
            print_error_message(ctx, error, "tried to use a command that is on cooldown")

        elif isinstance(error, commands.NotOwner):
            print_error_message(ctx, error, "tried to use a command that only the owner can use")

        elif isinstance(error, commands.MissingRole):
            print_error_message(ctx, error, "tried to use a command that requires a role they do not have")

        elif isinstance(error, commands.BotMissingPermissions):
            print_error_message(ctx, error, "tried to use a command that the bot does not have permission to use")

        else:
            print(Fore.RED + f"{time} - Error: {error}" + Fore.RESET)
    
    @commands.Cog.listener()
    async def on_slash_command(self, ctx):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = ctx.author.name
        print_event_message(self, time, author_name, "used a slash command")

    # Member-related Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = member.name
        print_event_message(self, time, author_name, "joined a server")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = member.name
        print_event_message(self, time, author_name, "left a server")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = user.name
        print_event_message(self, time, author_name, "was banned from a server")

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = user.name
        print_event_message(self, time, author_name, "was unbanned from a server")

    @commands.Cog.listener()
    async def on_member_kick(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = user.name
        print_event_message(self, time, author_name, "was kicked from a server")

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = before.name
        print_event_message(self, time, author_name, "updated their profile")

    # Message-related Events
    @commands.Cog.listener()
    async def on_message(self, message):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = message.author.name
        print_event_message(self, time, author_name, "sent a message")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = message.author.name
        print_event_message(self, time, author_name, "deleted a message")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = before.author.name
        print_event_message(self, time, author_name, "edited a message")

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = user.name
        print_event_message(self, time, author_name, "is typing")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = user.name
        print_event_message(self, time, author_name, "added a reaction")

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = user.name
        print_event_message(self, time, author_name, "removed a reaction")

    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = message.author.name
        print_event_message(self, time, author_name, "cleared a reaction")

    # Voice-related Events
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = member.name
        print_event_message(self, time, author_name, "updated their voice state")

    # Channel-related Events
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = channel.name
        print_event_message(self, time, author_name, "created a channel")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = channel.name
        print_event_message(self, time, author_name, "deleted a channel")

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = before.name
        print_event_message(self, time, author_name, "updated a channel")

    # Role-related Events
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = role.name
        print_event_message(self, time, author_name, "created a role")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = role.name
        print_event_message(self, time, author_name, "deleted a role")

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = before.name
        print_event_message(self, time, author_name, "updated a role")

    # Emoji-related Events
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = guild.name
        print_event_message(self, time, author_name, "updated an emoji")

    # Server-related Events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = guild.name
        print_event_message(self, time, author_name, "joined a server")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = guild.name
        print_event_message(self, time, author_name, "left a server")

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = before.name
        print_event_message(self, time, author_name, "updated a server")

    # Invite-related Events
    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = invite.inviter.name
        print_event_message(self, time, author_name, "created an invite")

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = invite.inviter.name
        print_event_message(self, time, author_name, "deleted an invite")

    # Webhook-related Events
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = channel.name
        print_event_message(self, time, author_name, "updated a webhook")

    # Integration-related Events
    @commands.Cog.listener()
    async def on_integration_create(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = integration.name
        print_event_message(self, time, author_name, "created an integration")

    @commands.Cog.listener()
    async def on_integration_delete(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = integration.name
        print_event_message(self, time, author_name, "deleted an integration")

    @commands.Cog.listener()
    async def on_integration_update(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = integration.name
        print_event_message(self, time, author_name, "updated an integration")

    # Stage-related Events
    @commands.Cog.listener()
    async def on_stage_instance_create(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = stage_instance.name
        print_event_message(self, time, author_name, "created a stage instance")

    @commands.Cog.listener()
    async def on_stage_instance_delete(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = stage_instance.name
        print_event_message(self, time, author_name, "deleted a stage instance")

    @commands.Cog.listener()
    async def on_stage_instance_update(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = stage_instance.name
        print_event_message(self, time, author_name, "updated a stage instance")

    # Thread-related Events
    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = thread.name
        print_event_message(self, time, author_name, "created a thread")

    @commands.Cog.listener()
    async def on_thread_delete(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = thread.name
        print_event_message(self, time, author_name, "deleted a thread")

    @commands.Cog.listener()
    async def on_thread_update(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = thread.name
        print_event_message(self, time, author_name, "updated a thread")

    @commands.Cog.listener()
    async def on_thread_member_join(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = thread.name
        print_event_message(self, time, author_name, "joined a thread")

    @commands.Cog.listener()
    async def on_thread_member_leave(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = thread.name
        print_event_message(self, time, author_name, "left a thread")

    @commands.Cog.listener()
    async def on_thread_member_update(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        author_name = thread.name
        print_event_message(self, time, author_name, "updated a thread")
        
async def setup(client):
    await client.add_cog(Logs(client))

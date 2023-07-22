import discord
import re
import json
import asyncio
from datetime import datetime
import os
from colorama import Fore, Back, Style
from discord.ext import commands

def hidden_users(self):
    with open('users.json', 'r') as f:
        users = json.load(f)
    return users['hidden']

def print_event_message(self, time, author_name, message):
    now = datetime.now()
    time = now.strftime("%H:%M")

    lower_author_name = author_name.name.lower()  # Directly work with the string representation of the username
    contains_bad_word = any(bad_word in lower_author_name for bad_word in self.bad_words)
    try:
        if contains_bad_word:
            filtered_author_name = re.sub(r'\b(?:' + '|'.join(map(re.escape, self.bad_words)) + r')\b', '#####', author_name, flags=re.IGNORECASE)
            print(Fore.GREEN + f"{time} - {filtered_author_name} {message}" + Fore.RESET)
        elif author_name.name in hidden_users(self):  # Compare with the list of hidden usernames
            print(Fore.GREEN + f"{time} - Hidden {message}" + Fore.RESET)
        else:
            print(Fore.GREEN + f"{time} - {author_name.name} {message}" + Fore.RESET)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")



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
                if author_name.id in hidden_users():
                    print(Fore.RED + f"{time} - Hidden {error_message}" + Fore.RESET)
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
        print_event_message(self, time, ctx.author, "used a slash command")

    # Member-related Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, member, "joined a server")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, member, "left a server")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, user, "was banned from a server")

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M") 
        print_event_message(self, time, user, "was unbanned from a server")

    @commands.Cog.listener()
    async def on_member_kick(self, guild, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, user, "was kicked from a server")

    # Message-related Events
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        now = datetime.now()
        time = now.strftime("%H:%M")
        try:
            print_event_message(time, guild, "left a server")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET}")


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        now = datetime.now()
        time = now.strftime("%H:%M")       
        print_event_message(self, time, message.author, "deleted a message")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, before.author, "edited a message")

    @commands.Cog.listener()
    async def on_typing(self, channel, user, when):
        now = datetime.now()
        time = now.strftime("%H:%M")        
        print_event_message(self, time, user, "is typing")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        now = datetime.now()
        time = now.strftime("%H:%M")    
        print_event_message(self, time, user, "added a reaction")

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, user, "removed a reaction")

    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, message.author, "cleared a reaction")

    # Voice-related Events
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        try:
            now = datetime.now()
            time = now.strftime("%H:%M")
            print_event_message(self, time, member, "updated their voice state")
        except Exception as e:
            print(f"{Fore.RED}Error: {e}{Fore.RESET}")

    # Channel-related Events
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, channel, "created a channel")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, channel, "deleted a channel")

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, before, "updated a channel")

    # Role-related Events
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, role, "created a role")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, role, "deleted a role")

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, before, "updated a role")

    # Emoji-related Events
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, guild, "updated an emoji")

    # Server-related Events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, guild, "joined a server")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, guild, "left a server")

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, before, "updated a server")

    # Invite-related Events
    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, invite.inviter, "created an invite")

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, invite.inviter, "deleted an invite")

    # Webhook-related Events
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, channel, "updated a webhook")

    # Integration-related Events
    @commands.Cog.listener()
    async def on_integration_create(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, integration, "created an integration")

    @commands.Cog.listener()
    async def on_integration_delete(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, integration, "deleted an integration")

    @commands.Cog.listener()
    async def on_integration_update(self, integration):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, integration, "updated an integration")

    # Stage-related Events
    @commands.Cog.listener()
    async def on_stage_instance_create(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, stage_instance, "created a stage instance")

    @commands.Cog.listener()
    async def on_stage_instance_delete(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, stage_instance, "deleted a stage instance")

    @commands.Cog.listener()
    async def on_stage_instance_update(self, stage_instance):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, stage_instance, "updated a stage instance")

    # Thread-related Events
    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, thread, "created a thread")

    @commands.Cog.listener()
    async def on_thread_delete(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, thread, "deleted a thread")

    @commands.Cog.listener()
    async def on_thread_update(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, thread, "updated a thread")

    @commands.Cog.listener()
    async def on_thread_member_join(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, thread, "joined a thread")

    @commands.Cog.listener()
    async def on_thread_member_leave(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, thread, "left a thread")

    @commands.Cog.listener()
    async def on_thread_member_update(self, thread):
        now = datetime.now()
        time = now.strftime("%H:%M")
        print_event_message(self, time, thread, "updated a thread")

async def setup(client):
    await client.add_cog(Logs(client))

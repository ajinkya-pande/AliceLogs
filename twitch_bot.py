import os
import json
import dotenv
import datetime
import twitchio
from twitchio.ext import commands

dotenv.load_dotenv()
token = os.getenv('TWITCH_BOT_TOKEN')

class TwitchLog(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.getenv("TMI_TOKEN"),
            client_id=os.getenv("CLIENT_ID"),
            nick=os.getenv("NICK"),
            prefix=os.getenv("BOT_PREFIX"),
            initial_channels=['alicelogs']
        )
        

    async def event_ready(self):
        print(f"Twitch Bot Ready | {self.nick}")

    async def event_usernotice_subscription(message):
        if message.tags.get("msg-id") == "sub":
            user = message.tags["display-name"]
            months = int(message.tags.get("msg-param-cumulative-months", 1))
            print(f"{user} just subscribed! ({months} months)")

        elif message.tags.get("msg-id") == "resub":
            user = message.tags["display-name"]
            months = int(message.tags.get("msg-param-cumulative-months", 1))
            print(f"{user} just resubscribed! ({months} months)")

        elif message.tags.get("msg-id") == "subgift":
            user = message.tags["display-name"]
            recipient = message.tags["msg-param-recipient-display-name"]
            print(f"{user} gifted a sub to {recipient}!")

        elif message.tags.get("msg-id") == "anonsubgift":
            recipient = message.tags["msg-param-recipient-display-name"]
            print(f"An anonymous user gifted a sub to {recipient}!")

        elif message.tags.get("msg-id") == "bitsbadgetier":
            user = message.tags["display-name"]
            bits = int(message.tags["msg-param-threshold"])
            print(f"{user} cheered {bits} bits!")

    async def event_usernotice_follow(self, message):
        user = message.tags["display-name"]
        print(f"{user} followed a channel!")
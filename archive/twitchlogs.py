import aiohttp, twitchio
import os
from twitchio.ext import commands
from colorama import Fore, Back, Style
from datetime import datetime
from dotenv import load_dotenv
from backend.log import twitch_event_msg

load_dotenv()

twitchbot = twitchio.ext.commands.Bot(
    token=os.getenv("TMI_TOKEN"),
    client_id=os.getenv("CLIENT_ID"),
    nick=os.getenv("NICK"),
    prefix=os.getenv("BOT_PREFIX"),
    initial_channels=['alicelogs']
)

# wen someone follows alicelogs on twitch
@twitchbot.event
async def event_usernotice_follow(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    twitch_event_msg(self, time, user, "followed alicelogs on twitch")

# when someone subs to alicelogs on twitch
@twitchbot.event
async def event_usernotice_subscription(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    months = int(message.tags.get("msg-param-cumulative-months", 1))
    twitch_event_msg(self, time, user, f"subscribed to alicelogs on twitch ({months} months)")
# when someone resubs to alicelogs on twitch
@twitchbot.event
async def event_usernotice_resubscription(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    months = int(message.tags.get("msg-param-cumulative-months", 1))
    twitch_event_msg(self, time, user, f"resubscribed to alicelogs on twitch ({months} months)")
# when someone gifts a sub to alicelogs on twitch
@twitchbot.event
async def event_usernotice_subgift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    recipient = message.tags["msg-param-recipient-display-name"]
    twitch_event_msg(self, time, user, f"gifted a sub to alicelogs on twitch ({recipient})")
# when someone gifts an anonymous sub to alicelogs on twitch
@twitchbot.event
async def event_usernotice_anonsubgift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    recipient = message.tags["msg-param-recipient-display-name"]
    twitch_event_msg(self, time, "Anonymous", f"gifted a sub to alicelogs on twitch ({recipient})")
# when someone cheers bits to alicelogs on twitch
@twitchbot.event
async def event_usernotice_bitsbadgetier(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    bits = int(message.tags["msg-param-threshold"])
    twitch_event_msg(self, time, user, f"cheered {bits} bits to alicelogs on twitch")
# when someone raids alicelogs on twitch
@twitchbot.event
async def event_usernotice_raid(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    viewers = int(message.tags["msg-param-viewerCount"])
    twitch_event_msg(self, time, user, f"raided alicelogs on twitch ({viewers} viewers)")
# when someone hosts alicelogs on twitch
@twitchbot.event
async def event_usernotice_host(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    viewers = int(message.tags["msg-param-viewerCount"])
    twitch_event_msg(self, time, user, f"hosted alicelogs on twitch ({viewers} viewers)")
# when someone gifts a raid to alicelogs on twitch
@twitchbot.event
async def event_usernotice_raidgift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    recipient = message.tags["msg-param-recipient-display-name"]
    viewers = int(message.tags["msg-param-viewerCount"])
    twitch_event_msg(self, time, user, f"gifted a raid to alicelogs on twitch ({recipient}, {viewers} viewers)")
# when someone gifts an anonymous raid to alicelogs on twitch
@twitchbot.event
async def event_usernotice_anonraidgift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    recipient = message.tags["msg-param-recipient-display-name"]
    viewers = int(message.tags["msg-param-viewerCount"])
    twitch_event_msg(self, time, "Anonymous", f"gifted a raid to alicelogs on twitch ({recipient}, {viewers} viewers)")
# when someone gifts a host to alicelogs on twitch
@twitchbot.event
async def event_usernotice_hostgift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    recipient = message.tags["msg-param-recipient-display-name"]
    viewers = int(message.tags["msg-param-viewerCount"])
    twitch_event_msg(self, time, user, f"gifted a host to alicelogs on twitch ({recipient}, {viewers} viewers)")
# when someone gifts an anonymous host to alicelogs on twitch
@twitchbot.event
async def event_usernotice_anonhostgift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    recipient = message.tags["msg-param-recipient-display-name"]
    viewers = int(message.tags["msg-param-viewerCount"])
    twitch_event_msg(self, time, "Anonymous", f"gifted a host to alicelogs on twitch ({recipient}, {viewers} viewers)")
# when someone gifts bits to alicelogs on twitch
@twitchbot.event
async def event_usernotice_ritual(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    bits = int(message.tags["msg-param-threshold"])
    twitch_event_msg(self, time, user, f"gifted bits to alicelogs on twitch ({bits} bits)")
# when someone gifts an anonymous bits to alicelogs on twitch
@twitchbot.event
async def event_usernotice_anonritual(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    bits = int(message.tags["msg-param-threshold"])
    twitch_event_msg(self, time, "Anonymous", f"gifted bits to alicelogs on twitch ({bits} bits)")

# when someone gifts a sub to alicelogs on twitch
@twitchbot.event
async def event_usernotice_submysterygift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    recipients = int(message.tags["msg-param-mass-gift-count"])
    twitch_event_msg(self, time, user, f"gifted a sub to alicelogs on twitch ({recipients} recipients)")
# when someone gifts an anonymous sub to alicelogs on twitch
@twitchbot.event
async def event_usernotice_anonsubmysterygift(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    recipients = int(message.tags["msg-param-mass-gift-count"])
    twitch_event_msg(self, time, "Anonymous", f"gifted a sub to alicelogs on twitch ({recipients} recipients)")
# when someone gifts a sub to alicelogs on twitch
@twitchbot.event
async def event_usernotice_giftpaidupgrade(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    user = message.tags["display-name"]
    recipient = message.tags["msg-param-recipient-display-name"]
    twitch_event_msg(self, time, user, f"gifted a sub to alicelogs on twitch ({recipient})")

# wen someone gifts an anonymous sub to alicelogs on twitch
@twitchbot.event
async def event_usernotice_anongiftpaidupgrade(self, message):
    now = datetime.now()
    time = now.strftime("%H:%M")
    recipient = message.tags["msg-param-recipient-display-name"]
    twitch_event_msg(self, time, "Anonymous", f"gifted a sub to alicelogs on twitch ({recipient})")
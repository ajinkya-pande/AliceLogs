import re
import json
import random
from datetime import datetime
from colorama import Fore, Back, Style

rainbow = [Fore.RED, Fore.CYAN, Fore.WHITE]

def hidden_users(self):
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    return users['hidden']

def print_event_message(self, time, author_name, message):
    with open("data/bad-words.txt") as file:
        self.bad_words = [bad_word.strip().lower() for bad_word in file]

    # open guilds.json
    with open('data/guilds.json', 'r') as f:
        guilds = json.load(f)

    now = datetime.now()
    time = now.strftime("%H:%M")

    lower_author_name = author_name.name.lower()  # Directly work with the string representation of the username
    contains_bad_word = any(bad_word in lower_author_name for bad_word in self.bad_words)
    try:
        if contains_bad_word:
            # if the guild is in guilds.json
            if author_name.guild.id in guilds:
                filtered_author_name = re.sub(r'\b(?:' + '|'.join(map(re.escape, self.bad_words)) + r')\b', '#####', author_name.name, flags=re.IGNORECASE)  # Use author_name.name as the string input for re.sub()
                print(random.choice(rainbow) + f"{time} - \x1b[38;5;75m[DISCORD]{Fore.RESET} " + random.choice(rainbow) + f"{filtered_author_name} {message}" + Fore.RESET)
            else:
                pass
        elif author_name.name in hidden_users(self):
            if author_name.guild.id in guilds:
                print(random.choice(rainbow) + f"{time} - \x1b[38;5;75m[DISCORD]{Fore.RESET} " + random.choice(rainbow) + f"Hidden {message}" + Fore.RESET)
            else:
                pass
        else:
            if author_name.guild.id in guilds:
                print(random.choice(rainbow) + f"{time} - \x1b[38;5;75m[DISCORD]{Fore.RESET} " + random.choice(rainbow) + f"{author_name.name} {message}" + Fore.RESET)
            else:
                pass
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")

def twitch_event_msg(self, time, author_name, message):
    with open("data/bad-words.txt") as file:
            self.bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]

    now = datetime.now()
    time = now.strftime("%H:%M")

    lower_author_name = author_name.lower()  # Directly work with the string representation of the username
    contains_bad_word = any(bad_word in lower_author_name for bad_word in self.bad_words)
    try:
        if contains_bad_word:
            filtered_author_name = re.sub(r'\b(?:' + '|'.join(map(re.escape, self.bad_words)) + r')\b', '#####', author_name, flags=re.IGNORECASE)  # Use author_name.name as the string input for re.sub()
            print(Fore.GREEN + f"{time} - " + '\x1b[38;5;141m' + f"[TWITCH]{Fore.RESET}{Fore.GREEN} {filtered_author_name} {message}" + Fore.RESET)
        elif author_name in hidden_users(self):  # Compare with the list of hidden usernames
            print(Fore.GREEN + f"{time} - " + '\x1b[38;5;141m' + f"[TWITCH]{Fore.RESET}{Fore.GREEN} Hidden {message}" + Fore.RESET)
        else:
            print(Fore.GREEN + f"{time} - " + '\x1b[38;5;141m' + f"[TWITCH]{Fore.RESET}{Fore.GREEN} {author_name} {message}" + Fore.RESET)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")
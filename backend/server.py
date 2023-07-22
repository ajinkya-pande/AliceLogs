import socket
import re
import json
from datetime import datetime
from colorama import Fore, Back, Style

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2020))
s.listen(5)

def hidden_users(self):
    with open('users.json', 'r') as f:
        users = json.load(f)
    return users['hidden']

while True:
    clientsocket, address = s.accept()
    print(f"Connection has been established!")
    def print_event_message(self, time, author_name, message):
        now = datetime.now()
        time = now.strftime("%H:%M")

        lower_author_name = author_name.name.lower()  # Directly work with the string representation of the username
        contains_bad_word = any(bad_word in lower_author_name for bad_word in self.bad_words)
        try:
            if contains_bad_word:
                filtered_author_name = re.sub(r'\b(?:' + '|'.join(map(re.escape, self.bad_words)) + r')\b', '#####', author_name.name, flags=re.IGNORECASE)  # Use author_name.name as the string input for re.sub()
                clientsocket.send(bytes(Fore.GREEN + f"{time} - {Fore.BLUE}[DISCORD]{Fore.RESET}{Fore.GREEN} {filtered_author_name} {message}" + Fore.RESET, "utf-8"))
            elif author_name.name in hidden_users(self):  # Compare with the list of hidden usernames
                clientsocket.send(bytes(Fore.GREEN + f"{time} - {Fore.BLUE}[DISCORD]{Fore.RESET}{Fore.GREEN} Hidden {message}" + Fore.RESET, "utf-8"))
            else:
                clientsocket.send(bytes(Fore.GREEN + f"{time} - {Fore.BLUE}[DISCORD]{Fore.RESET}{Fore.GREEN} {author_name.name} {message}" + Fore.RESET, "utf-8"))
        except Exception as e:
            clientsocket.send(bytes(f"{Fore.RED}Error: {e}{Fore.RESET}", "utf-8"))
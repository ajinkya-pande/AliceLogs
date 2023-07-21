# AliceLogs Discord Bot

AliceLogs is a Discord bot designed to log various events happening in a server. It tracks actions such as user joins, message edits, reactions, channel updates, and much more. The bot provides a comprehensive log of server activities, helping administrators keep track of what's happening in their community.

## Features

- Log various server events, including member actions, messages, reactions, and more.
- Filter out messages from users using a predefined list of bad words.
- Provides real-time logging and updates.
- Organizes events into categories for easy management.

## Requirements

- Python 3.6+
- discord.py library (version 1.7.3 or higher)
- colorama library (for colored console output)

## Installation

1. Clone this repository to your local machine:
```
git clone https://github.com/yourusername/AliceLogs.git
cd AliceLogs
```

2. Install the required Python packages:
```
pip install -r requirements.txt
```

3. Create a file named `data/bad-words.txt` and add any inappropriate words or phrases to be filtered out from user names.

4. Obtain a Discord Bot token by creating a new bot application on the [Discord Developer Portal](https://discord.com/developers/applications). Copy the token and keep it secure.

5. Replace the `YOUR_BOT_TOKEN_HERE` placeholder in the `.env` file with your actual bot token.

6. Run the bot:
```
python bot.py
```


## Usage

Once the bot is up and running, it will automatically start logging various events in the server. The logs will be displayed in the console with different colors for easy identification:

- Green: Regular events, such as user joins, messages, etc.
- Red: Command errors and forbidden actions.
- Yellow: Channel, role, or server updates.
- Blue: Slash commands.

Please note that the bot will only log events that occur while it is active. To maintain continuous logging, it is recommended to keep the bot running 24/7.

## Customization

The bot can be customized to log additional events or ignore certain actions based on specific needs. The event handlers can be modified or extended in the `bot.py` file.

## Contributing

If you'd like to contribute to AliceLogs, feel free to open a pull request with your proposed changes. Any contributions, bug fixes, or improvements are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

AliceLogs is a hobby project and provided as-is without any warranty. Use it at your own risk, and always be mindful of Discord's Terms of Service and Community Guidelines. The developers of this bot are not responsible for any misuse or actions taken based on the information logged by the bot.

## Links

- Add the bot: [Universe List](https://universe-list.xyz/bots/1131451736247255091)
- Support: [Discord Server](https://discord.gg/6dCMQt33aw)
- Vote for me: [Universe List](https://universe-list.xyz/bots/1131451736247255091)
- Invite me: [Discord Invite](https://discord.com/api/oauth2/authorize?client_id=1131451736247255091&permissions=2611341028544&scope=bot)


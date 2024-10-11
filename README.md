# User ID Fetcher by Nickname

This project is a Python-based bot built using the `Aiogram` and `Telethon` libraries. It fetches the Telegram user ID by their nickname and includes validation to ensure the nickname is valid.

## Features

- Fetches user ID by providing their Telegram nickname.
- Validates the format of the nickname to avoid errors.
- Asynchronous and lightweight, built with `Aiogram` and `Telethon`.

## Prerequisites

- Python 3.8+
- A Telegram bot token
- A Telegram API ID and API hash (you can get these from [Telegram's API development page](https://my.telegram.org/auth))
- The following Python libraries:
  - `aiogram`
  - `telethon`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dimakostenko19/aiogram_id.git
   cd get_user-id

2. **Install dependencies**:
```bash
    pip install -r requirements.txt
```

3. **Replace the token, api_id, and api_hash in api.py**:
    - Open api.py
    - Find and replace the placeholder values with your actual bot token, api_id, and api_hash:
```bash
TOKEN = "your_bot_token_here"
api_id = "your_api_id_here"
api_hash = "your_api_hash_here"
```

### Usage
1. Start the bot:
```bash
python bot.py
```
2. Send the bot a nickname, and it will return the corresponding user ID, provided the nickname is valid.

#### Validation
The bot includes nickname validation to ensure the provided nickname is a valid Telegram username.
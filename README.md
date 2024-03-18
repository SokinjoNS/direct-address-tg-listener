# Direct Address Telegram Listener

The __direct_address_tg_listener.py__ module is one of essential components of Telegram bot application, specifically designed to detect and process Ethereum addresses directly shared in Telegram messages. Upon detection, it utilizes the __telegram_alerts.py__ module to send formatted alerts to a specified Telegram chat or channel.

## Features

- __Ethereum Address Detection:__ Automatically identifies Ethereum addresses within the text of Telegram messages.
- __Alert Integration:__ Sends notifications with detected Ethereum address details using the __telegram_alerts.py__ module.
- __Scalable and Extensible:__ Easily extendable to include additional functionalities such as address validation or interaction with blockchain APIs.

## Getting Started

__Prerequisites__

- Python 3.6 or newer.
- A registered Telegram bot with access to the Telegram API.
- The Telethon library installed for Telegram API interactions.
- Proper configuration in the __telegram_alerts.py__ module for alert messaging.

__Installation__

__1. Verify Python Installation:__

Confirm that Python 3.6+ and __pip__ are installed on your system.

__2. Install Telethon:__

If not already present, install the Telethon package:

```bash
pip install telethon
```

__3. Set Up Bot Credentials:__

Ensure your __credentials_telegram.json__ file is correctly configured with your __api_id__, __api_hash__, and __bot_token__.

## Usage

__direct_address_tg_listener.py__ is designed to be integrated within the Telegram bot's main message processing flow:

__1. Import and Use in Main Script:__

The main listener script (__tg_message_listener_main.py__) should import and use this module to process messages that potentially contain direct Ethereum addresses.

__2. Run Your Telegram Bot:__

Execute your bot's main script to start listening for and processing messages:

```bash
python tg_message_listener_main.py
```

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Support

For issues, questions, or contributions, please open an issue in the GitHub repository.

Feedback and contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

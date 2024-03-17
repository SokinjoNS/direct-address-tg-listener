import re
import json
from telegram_alerts import handle_and_send_message

def load_telegram_credentials():
    with open('credentials_telegram.json') as f:
        credentials = json.load(f)
    return credentials

def is_direct_token_address(message):
    contract_pattern = re.compile(r'0x[a-fA-F0-9]{40}')
    match = contract_pattern.search(message)
    return match.group() if match else None

def handle_direct_address_message(message):
    credentials = load_telegram_credentials()
    token_address = is_direct_token_address(message)
    if token_address:
        details = {
            'token_address': token_address,
            'source': 'Direct Address',
        }
        handle_and_send_message('direct_address', details, credentials)
    else:
        print("No direct Ethereum address detected.")

import requests

def send_telegram_message(bot_token, chat_id, message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    requests.post(url, json=payload)

bot_token = "REPLACE WITH YOUR BOT TOKEN"
chat_id = "REPLACE WITH YOUR CHAT ID"

message = 'Torrent Complete'
send_telegram_message(bot_token, chat_id, message)

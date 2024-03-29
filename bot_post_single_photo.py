import argparse
import os
import random
import telegram
from dotenv import load_dotenv
from common_functions import collect_photo_filenames


def set_cli_args():
    parser = argparse.ArgumentParser(description='telegram bot sends random space photo into tg channel')
    parser.add_argument('-n', '--filename', type=str, help='enter photo filename',
                        default=random.choice(collect_photo_filenames()))
    return parser


def post_single_photo(bot, chat_id, post_photo):
    with open(f'images/{post_photo}', 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


def main():
    parser = set_cli_args()
    cli_args = parser.parse_args()
    load_dotenv()
    chat_id = os.environ['TG_CHAT_ID']
    bot_token = os.environ['TG_BOT_TOKEN']
    bot = telegram.Bot(bot_token)
    post_single_photo(bot=bot, chat_id=chat_id, post_photo=cli_args.filename)


if __name__ == '__main__':
    main()

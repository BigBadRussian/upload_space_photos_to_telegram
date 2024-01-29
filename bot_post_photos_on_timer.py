import os
import random
import time
import argparse
import telegram
from dotenv import load_dotenv
from common_functions import collect_photo_filenames


def set_cli_args():
    parser = argparse.ArgumentParser(description='telegram bot sends random space photo '
                                                 'into tg channel at certain time intervals')
    parser.add_argument('-t', '--timer', type=int, help='enter time period for posts (secs)', default=14400)
    return parser


def send_photos_one_per_time(bot, chat_id, post_timer):
    file_names = collect_photo_filenames()
    while file_names:
        post_photo = random.choice(file_names)
        with open(f'images/{post_photo}', 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
        file_names.remove(post_photo)
        time.sleep(post_timer)


def main():
    parser = set_cli_args()
    args = parser.parse_args()
    load_dotenv()
    chat_id = os.environ['TG_CHAT_ID']
    bot_token = os.environ['TG_BOT_TOKEN']
    bot = telegram.Bot(bot_token)
    while True:
        send_photo_on_time(bot=bot, chat_id=chat_id, post_timer=args.timer)


if __name__ == '__main__':
    main()

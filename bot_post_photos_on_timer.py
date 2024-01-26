import os
import random
import time
import argparse
import telegram
from dotenv import load_dotenv
from common_functions import collect_photo_filenames


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Download spaceX launch photo')
    parser.add_argument('-t', '--timer', type=int, help='enter time period for posts (secs)', default=14400)
    args = parser.parse_args()
    return args


def send_photo_on_time(bot, chat_id):
    file_names = collect_photo_filenames()
    post_timer = create_arg_parser().timer
    while file_names:
        post_photo = random.choice(file_names)
        with open(f'images/{post_photo}', 'rb') as file:
            photo = file
            bot.send_photo(chat_id=chat_id, photo=photo)
        file_names.remove(post_photo)
        time.sleep(post_timer)


def main():
    load_dotenv()
    chat_id = os.environ['TG_CHAT_ID']
    bot_token = os.environ['TG_BOT_TOKEN']
    bot = telegram.Bot(bot_token)
    while True:
        send_photo_on_time(bot=bot, chat_id=chat_id)


if __name__ == '__main__':
    main()

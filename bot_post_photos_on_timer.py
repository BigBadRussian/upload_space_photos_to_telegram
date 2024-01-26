import random
import time
import argparse
from common_functions import create_bot, collect_photo_filenames


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Download spaceX launch photo')
    parser.add_argument('-t', '--timer', type=int, help='enter time period for posts (secs)', default=14400)
    args = parser.parse_args()
    return args


def send_photo_on_time():
    file_names = collect_photo_filenames()
    post_timer = create_arg_parser().timer
    bot, chat_id = create_bot()
    while file_names:
        post_photo = random.choice(file_names)
        bot.send_photo(chat_id=chat_id, photo=open(f'images/{post_photo}', 'rb'))
        file_names.remove(post_photo)
        time.sleep(post_timer)
    if not file_names:
        send_photo_on_time()


def main():
    send_photo_on_time()


if __name__ == '__main__':
    main()

import argparse
import random
from common_functions import create_bot, collect_photo_filenames


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Download spaceX launch photo')
    parser.add_argument('-n', '--filename', type=str, help='enter photo filename', default=None)
    args = parser.parse_args()
    return args


def post_single_photo():
    bot, chat_id = create_bot()
    if create_arg_parser().filename:
        post_photo = create_arg_parser().filename
    else:
        post_photo = random.choice(collect_photo_filenames())
    bot.send_photo(chat_id=chat_id, photo=open(f'images/{post_photo}', 'rb'))


if __name__ == '__main__':
    post_single_photo()

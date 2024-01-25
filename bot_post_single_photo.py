import random

from common_functions import arg_parser, create_bot, collect_photo_filenames


def post_single_photo():
    bot, chat_id = create_bot()
    if arg_parser().filename:
        post_photo = arg_parser().filename
    else:
        post_photo = random.choice(collect_photo_filenames())
    bot.send_photo(chat_id=chat_id, photo=open(f'images/{post_photo}', 'rb'))


if __name__ == '__main__':
    post_single_photo()

from common_functions import arg_parser, create_bot


def post_single_photo():
    bot, chat_id = create_bot()
    post_photo = arg_parser().filename
    bot.send_photo(chat_id=chat_id, photo=open(f'images/{post_photo}', 'rb'))


if __name__ == '__main__':
    post_single_photo()
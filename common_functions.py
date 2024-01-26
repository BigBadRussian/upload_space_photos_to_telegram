import os
from urllib.parse import urlsplit
import requests
import telegram
from dotenv import load_dotenv


def create_photo_folder():
    if not os.path.exists('images'):
        os.makedirs('images')


def collect_photo_filenames():
    folder_path = 'images'
    file_names = []
    for entry in os.scandir(folder_path):
        if entry.is_file():
            file_names.append(entry.name)
    return file_names


def download_image(url, path_to_file):
    response = requests.get(url)
    response.raise_for_status()
    with open(path_to_file, 'wb') as file:
        file.write(response.content)


def get_image_extension(image_url):
    path = urlsplit(image_url).path
    image_filename = os.path.split(path)[1]
    image_extension = os.path.splitext(image_filename)[1]
    return image_extension


def create_bot():
    load_dotenv()
    chat_id = os.environ['CHAT_ID']
    bot_token = os.environ['BOT_TOKEN']
    bot = telegram.Bot(bot_token)
    return bot, chat_id

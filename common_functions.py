import os
from urllib.parse import urlsplit
import requests


def collect_photo_filenames():
    folder_path = 'images'
    file_names = []
    for entry in os.scandir(folder_path):
        if entry.is_file():
            file_names.append(entry.name)
    return file_names


def download_image(url, params, full_filename):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(full_filename, 'wb') as file:
        file.write(response.content)


def get_image_extension(image_url):
    path = urlsplit(image_url).path
    image_filename = os.path.split(path)[1]
    image_extension = os.path.splitext(image_filename)[1]
    return image_extension

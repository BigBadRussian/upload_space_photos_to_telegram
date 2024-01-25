import os
import requests
from dotenv import load_dotenv
from common_functions import download_image, create_photo_folder, get_image_extension, arg_parser


def get_nasa_link_apod(count):
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    list_image_url = []
    for i, item in enumerate(response.json()):
        list_image_url.append(item['url'])
    return list_image_url


def main():
    create_photo_folder()
    for i, link in enumerate(get_nasa_link_apod(arg_parser().count), 1):
        download_image(link, path_to_file=f"images/nasa_apod_photo_{i}{get_image_extension(link)}")


if __name__ == "__main__":
    main()

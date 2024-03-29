import argparse
import os
import requests
from dotenv import load_dotenv
from common_functions import download_image, get_image_extension


def set_cli_args():
    parser = argparse.ArgumentParser(description='Download nasa apod photo')
    parser.add_argument('-c', '--count', type=int, help='enter count of photos', default=5)
    return parser


def get_nasa_apod_image_links(count, nasa_token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_apod_image_links = [item['url'] for item in response.json()]
    return nasa_apod_image_links


def main():
    parser = set_cli_args()
    cli_args = parser.parse_args()
    os.makedirs('images', exist_ok=True)
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    params = {'api_key': nasa_token}
    apod_image_links = get_nasa_apod_image_links(cli_args.count, nasa_token=nasa_token)
    filename_template = "images/nasa_apod_photo_"
    for number, link in enumerate(apod_image_links):
        download_image(link, params=params, full_filename=f"{filename_template}{number}{get_image_extension(link)}")


if __name__ == "__main__":
    main()

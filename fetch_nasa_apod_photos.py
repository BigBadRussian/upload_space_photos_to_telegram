import argparse
import os
import requests
from dotenv import load_dotenv
from common_functions import download_image, get_image_extension


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Download spaceX launch photo')
    parser.add_argument('-c', '--count', type=int, help='enter count of photos', default=5)
    args = parser.parse_args()
    return args


def get_nasa_apod_image_links(count, nasa_token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_apod_image_links = [item['url'] for item in response.json()]
    return nasa_apod_image_links


def main():
    os.makedirs('images', exist_ok=True)
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    params = {'api_key': nasa_token}
    for i, link in enumerate(get_nasa_apod_image_links(create_arg_parser().count, nasa_token=nasa_token),  1):
        download_image(link, params=params, path_to_file=f"images/nasa_apod_photo_{i}{get_image_extension(link)}")


if __name__ == "__main__":
    main()

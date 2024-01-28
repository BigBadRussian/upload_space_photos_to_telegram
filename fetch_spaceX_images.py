import argparse
import os
import requests
from common_functions import download_image


def set_cli_args():
    parser = argparse.ArgumentParser(description='Download spaceX launch photo')
    parser.add_argument('-l', '--launch_id', type=str, help='enter launch_id',
                        default='61eefaa89eb1064137a1bd73')
    return parser


def get_spaceX_launch_image_links(launch_id):
    url_space_x = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url_space_x)
    response.raise_for_status()
    pic_links = response.json()["links"]["flickr"]["original"]
    return pic_links


def main():
    parser = set_cli_args()
    cli_args = parser.parse_args()
    os.makedirs('images', exist_ok=True)
    filename_template = 'images/spaceX_'
    image_extension = '.jpg'
    for number, link in enumerate(get_spaceX_launch_image_links(launch_id=cli_args.launch_id), 1):
        download_image(link, params=None, full_filename=f'{filename_template}{number}{image_extension}')


if __name__ == "__main__":
    main()

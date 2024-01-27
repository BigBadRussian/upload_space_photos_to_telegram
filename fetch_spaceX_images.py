import argparse
import os

import requests
from common_functions import download_image


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Download spaceX launch photo')
    parser.add_argument('-l', '--launch_id', type=str, help='enter launch_id',
                        default='61eefaa89eb1064137a1bd73')
    args = parser.parse_args()
    return args


def get_spaceX_launch_image_links():
    launch_id = create_arg_parser().launch_id
    url_space_x = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url_space_x)
    response.raise_for_status()
    pic_links = response.json()["links"]["flickr"]["original"]
    return pic_links


def main():
    os.makedirs('images', exist_ok=True)
    for i, link in enumerate(get_spaceX_launch_image_links(), 1):
        download_image(link, params=None, path_to_file=f"images/spaceX_{i}.jpg")


if __name__ == "__main__":
    main()

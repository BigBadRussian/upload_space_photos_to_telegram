import requests
from common_functions import download_image, create_photo_folder, arg_parser


def get_pics_links_from_spaceX_launch():
    launch_id = arg_parser().launch_id
    url_space_x = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url_space_x)
    response.raise_for_status()
    pic_links = response.json()["links"]["flickr"]["original"]
    return pic_links


def main():
    create_photo_folder()
    for i, link in enumerate(get_pics_links_from_spaceX_launch(), 1):
        download_image(link, path_to_file=f"images/spaceX_{i}.jpg")


if __name__ == "__main__":
    main()

import os
import requests
from dotenv import load_dotenv
from common_functions import download_image


def get_nasa_epic_image_properties(nasa_token):
    epic_photos_properties_url = f'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': nasa_token}
    response = requests.get(epic_photos_properties_url, params=params)
    response.raise_for_status()
    return response.json()


def compose_nasa_epic_image_links(nasa_token):
    image_properties = get_nasa_epic_image_properties(nasa_token)
    epic_photo_archive_url = f'https://api.nasa.gov/EPIC/archive/natural'
    photo_filenames_and_dates = [{'filename': f'{item["image"]}.png',
                                  'date': '/'.join(item['date'].split()[0].split('-'))}
                                 for item in image_properties]
    epic_photo_urls = [f'{epic_photo_archive_url}/{photo_filenames_and_dates[i]["date"]}/png/'
                       f'{photo_filenames_and_dates[i]["filename"]}'
                       for i, item in enumerate(photo_filenames_and_dates)]

    return epic_photo_urls


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    params = {'api_key': nasa_token}
    os.makedirs('images', exist_ok=True)
    filename_template = f"images/nasa_epic_photo_"
    image_extension = ".png"
    image_links = compose_nasa_epic_image_links(nasa_token=nasa_token)
    for i, link in enumerate(image_links):
        download_image(link, params=params, full_filename=f"{filename_template}{i}{image_extension}")


if __name__ == "__main__":
    main()

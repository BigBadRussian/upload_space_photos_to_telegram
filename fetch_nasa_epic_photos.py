import os
import requests
from dotenv import load_dotenv
from common_functions import download_image


def get_nasa_epic_image_links(nasa_token):
    epic_photos_data_url = f'https://api.nasa.gov/EPIC/api/natural/images'
    params_apikey = {'api_key': nasa_token}
    epic_photo_file_url = f'https://api.nasa.gov/EPIC/archive/natural'
    response = requests.get(epic_photos_data_url, params=params_apikey)
    response.raise_for_status()
    photo_filenames = [f'{item["image"]}.png' for item in response.json()]
    photo_dates = ['/'.join(item['date'].split()[0].split('-')) for item in response.json()]
    photo_filenames_dates = [{'filename': x, 'date': y} for x, y in zip(photo_filenames, photo_dates)]
    epic_photo_urls = [f'{epic_photo_file_url}/{photo_filenames_dates[i]["date"]}/png/'
                       f'{photo_filenames_dates[i]["filename"]}?api_key={nasa_token}'
                       for i, item in enumerate(photo_filenames_dates)]

    return epic_photo_urls


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    os.makedirs('images', exist_ok=True)
    for i, link in enumerate(get_nasa_epic_image_links(nasa_token=nasa_token), 1):
        download_image(link, path_to_file=f"images/nasa_epic_photo{i}.png")


if __name__ == "__main__":
    main()

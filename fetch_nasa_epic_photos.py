import os
import requests
from dotenv import load_dotenv
from common_functions import create_photo_folder, download_image


def get_nasa_epic_image_links(nasa_token):
    url_data_photos = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={nasa_token}'
    url_photo_file = f'https://api.nasa.gov/EPIC/archive/natural'
    response = requests.get(url_data_photos)
    response.raise_for_status()
    data_photos = response.json()
    photo_filenames = []
    photo_dates = []
    for i, item in enumerate(data_photos):
        photo_filenames.append(f'{item["image"]}.png')
        photo_dates.append('/'.join(item['date'].split()[0].split('-')))

    new_epic_data = []
    for i, item in enumerate(data_photos):
        new_epic_data.append({'filename': photo_filenames[i], 'date': photo_dates[i]})

    epic_photo_urls = []
    for i, item in enumerate(new_epic_data):
        epic_photo_urls.append(f'{url_photo_file}/{new_epic_data[i]["date"]}/png/'
                               f'{new_epic_data[i]["filename"]}?api_key={nasa_token}')
    return epic_photo_urls


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    create_photo_folder()
    for i, link in enumerate(get_nasa_epic_image_links(nasa_token=nasa_token), 1):
        download_image(link, path_to_file=f"images/nasa_epic_photo{i}.png")


if __name__ == "__main__":
    main()

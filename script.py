import requests
from dotenv import load_dotenv
from urllib.parse import urlsplit
import os


def download_image(url, path_to_file):
    response = requests.get(url)
    response.raise_for_status()
    with open(path_to_file, 'wb') as file:
        file.write(response.content)


def get_pics_links_from_spaceX_launch():
    launch_id = '5eb87ce3ffd86e000604b336'
    url_space_x = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url_space_x)
    response.raise_for_status()
    pic_links = response.json()["links"]["flickr"]["original"]
    return pic_links


def get_nasa_link_apod():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    list_image_url = []
    for i, item in enumerate(response.json()):
        list_image_url.append(item['hdurl'])
    return list_image_url


def get_image_extension(image_url):
    path = urlsplit(image_url).path
    image_filename = os.path.split(path)[1]
    image_extension = os.path.splitext(image_filename)[1]
    return image_extension


def get_nasa_epic_photo():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={nasa_token}'


def get_epic_nasa_urls():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
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
    if not os.path.exists('images'):
        os.makedirs('images')
    pic_links = get_pics_links_from_spaceX_launch()
    for i, link in enumerate(pic_links):
        download_image(link, path_to_file=f"images/spaceX_{i}.jpg")
    for i, link in enumerate(get_nasa_link_apod(), 1):
        download_image(link, path_to_file=f"images/nasa_photo_{i}{get_image_extension(link)}")
    for i, link in enumerate(get_epic_nasa_urls(), 1):
        download_image(link, path_to_file=f"images/nasa_epic_photo{i}.png")


if __name__ == '__main__':
    main()

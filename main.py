import requests
import os
import datetime
from pathlib import Path
from urllib.parse import urlparse, unquote
from dotenv import load_dotenv


SPACEX_URL = 'https://api.spacexdata.com/v5/launches/5eb87ce4ffd86e000604b338'
APOD_URL = 'https://api.nasa.gov/planetary/apod'
EPIC_URL = 'https://api.nasa.gov/EPIC/api/natural'
EPIC_URL2 = 'https://api.nasa.gov/EPIC/archive/natural/'
directory = 'images/'
if not os.path.exists(directory):
    os.makedirs(directory)


def dwnld_jpg(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def file_ext(url):
    url = urlparse(unquote(url))
    return os.path.splitext(url.path)[1]


def fetch_spacex_last_launch():
    response = requests.get(SPACEX_URL)
    response.raise_for_status()
    jpeg_list = response.json()["links"]["flickr"]['original']
    for jpeg_num, jpeg in enumerate(jpeg_list):
        filename = os.path.join('{}{}{}{}'.format(directory, 'spacex', str(jpeg_num), file_ext(jpeg)))
        dwnld_jpg(jpeg, filename)


def fetch_apod(header):
    jpeg_list = []
    response = requests.get(APOD_URL, header)
    response.raise_for_status()
    json_list = response.json()
    for jpeg in json_list:
        jpeg_list.append(jpeg["url"])
    for jpeg_num, jpeg in enumerate(jpeg_list):
        filename = os.path.join('{}{}{}{}'.format(directory, 'nasa_apod_', str(jpeg_num), file_ext(jpeg)))
        dwnld_jpg(jpeg, filename)


def fetch_epic(header1, header2):
    jpeg_list = []
    response = requests.get(EPIC_URL, header1)
    response.raise_for_status()
    json_list = response.json()
    for jpeg in json_list:
        date_jpeg, name_jpeg = datetime.datetime.fromisoformat(jpeg["date"]), jpeg['image']
        jpeg_list.append('{}{}{}{}{}'.format(EPIC_URL2, str(date_jpeg.strftime("%Y/%m/%d")), '/png/', name_jpeg, '.png'))
    for jpeg_num, jpeg in enumerate(jpeg_list):
        response = requests.get(jpeg, header2)
        filename = os.path.join('{}{}{}{}'.format(directory, 'nasa_epic_', str(jpeg_num), file_ext(jpeg)))
        dwnld_jpg(response.url, filename)


def main():
    load_dotenv()
    token = os.environ["APOD_TOKEN"]
    fetch_spacex_last_launch()
    fetch_apod({'count': 30, 'api_key': token})
    fetch_epic({'count': 10, 'api_key': token}, {'api_key': token})


if __name__ == '__main__':
    main()

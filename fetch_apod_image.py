import requests
import os
from urllib.parse import urlparse, unquote
from download_jpg_and_file_extension import *
from dotenv import load_dotenv


APOD_URL = 'https://api.nasa.gov/planetary/apod'


def fetch_apod(header):
    jpeg_list = []
    response = requests.get(APOD_URL, header)
    response.raise_for_status()
    json_list = response.json()
    for jpeg in json_list:
        jpeg_list.append(jpeg["url"])
    for jpeg_num, jpeg in enumerate(jpeg_list):
        filename = os.path.join('{}{}{}{}'.format('images/', 'nasa_apod_', str(jpeg_num), file_ext(jpeg)))
        dwnld_jpg(jpeg, filename)


def main():
    if not os.path.exists('images/'):
        os.makedirs('images/')
    load_dotenv()
    apod_token = os.environ["APOD_TOKEN"]
    fetch_apod({'count': 30, 'api_key': apod_token})


if __name__ == '__main__':
    main()

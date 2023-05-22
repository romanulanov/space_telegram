import requests
import os
from urllib.parse import urlparse, unquote
from download_image_and_file_extension import dwnld_image, get_file_ext
from dotenv import load_dotenv


APOD_URL = 'https://api.nasa.gov/planetary/apod'


def fetch_apod(header):
    image_list = []
    response = requests.get(APOD_URL, header)
    response.raise_for_status()
    json_list = response.json()
    for image in json_list:
        image_list.append(image["url"])
    for image_num, image in enumerate(image_list):
        filename = os.path.join('{}{}{}{}'.format('images/', 'nasa_apod_', str(image_num), get_file_ext(image)))
        dwnld_image(image, filename)


def main():
    if not os.path.exists('images/'):
        os.makedirs('images/')
    load_dotenv()
    apod_token = os.environ["APOD_TOKEN"]
    fetch_apod({'count': 30, 'api_key': apod_token})


if __name__ == '__main__':
    main()

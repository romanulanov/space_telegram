import requests
import os
from urllib.parse import urlparse, unquote
from download_image_and_file_extension_and_get_images import dwnld_image, get_file_ext
from dotenv import load_dotenv


APOD_URL = 'https://api.nasa.gov/planetary/apod'


def fetch_apod(header):
    response = requests.get(APOD_URL, header)
    response.raise_for_status()
    response = response.json()
    images = []
    for image in response:
        if image["media_type"] == "image":
            if image["hdurl"]:
                images.append(image["hdurl"])
            images.append(image["url"])
    for image_num, image in enumerate(images):
        filename = os.path.join('{}{}{}{}'.format('images/', 'nasa_apod_', str(image_num), get_file_ext(image)))
        dwnld_image(image, filename)


def main():
    load_dotenv()
    os.makedirs('images/', exist_ok=True)
    apod_token = os.environ["APOD_TOKEN"]
    fetch_apod({'count': 30, 'api_key': apod_token})


if __name__ == '__main__':
    main()

import requests
import os
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
        filename = os.path.join('{}{}{}{}'.format('images/', 'nasa_apod_', image_num, get_file_ext(image)))
        dwnld_image(image, filename)


def main():
    load_dotenv()
    os.makedirs('images/', exist_ok=True)
    nasa_token = os.environ["NASA_TOKEN"]
    count = 30
    fetch_apod({'count': count, 'api_key': nasa_token})


if __name__ == '__main__':
    main()

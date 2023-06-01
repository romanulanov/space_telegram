import requests
import os
import argparse
from utils import download_image, get_file_ext
from dotenv import load_dotenv


APOD_URL = 'https://api.nasa.gov/planetary/apod'


def fetch_apod(header, count, path):
    response = requests.get(APOD_URL, header)
    response.raise_for_status()
    response = response.json()
    images = []
    for image in response:
        if image["media_type"] == "image":
            if image["hdurl"]:
                images.append(image["hdurl"])
            images.append(image["url"])
    images = images[:count]
    for image_num, image in enumerate(images):
        filename = os.path.join('{}{}{}{}'.format(path, 'nasa_apod_', image_num, get_file_ext(image)))
        download_image(image, filename)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='images', help='Введите название папки (по умолчанию images)')
    parser.add_argument('--count', type=int, default=30, help='Введите количество фото, которое надо скачать (по умолчанию 30)')
    args = parser.parse_args()
    os.makedirs(args.path, exist_ok=True)
    nasa_token = os.environ["NASA_TOKEN"]
    fetch_apod({'count': args.count, 'api_key': nasa_token}, args.count, f"{args.path}{'/'}")


if __name__ == '__main__':
    main()

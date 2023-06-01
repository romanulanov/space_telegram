import requests
import os
import argparse
from utils import dwnld_image, get_file_ext


SPACEX_URL = 'https://api.spacexdata.com/v5/launches/'


def fetch_spacex_last_launch(path, launch_id):
    response = requests.get(f"{SPACEX_URL}{launch_id}")
    response.raise_for_status()
    images = response.json()["links"]["flickr"]['original']
    for image_num, image in enumerate(images):
        filename = os.path.join('{}{}{}{}'.format(path, 'spacex', image_num, get_file_ext(image)))
        dwnld_image(image, filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='images', help='Введите название папки (по умолчанию images)')
    parser.add_argument('--id', default='5eb87ce4ffd86e000604b338', help='Введите id полёта, фото которого надо скачать (по умолчанию 5eb87ce4ffd86e000604b338)')
    args = parser.parse_args()
    os.makedirs(args.path, exist_ok=True)
    fetch_spacex_last_launch(f"{args.path}{'/'}", args.id) 
 

if __name__ == '__main__':
    main()

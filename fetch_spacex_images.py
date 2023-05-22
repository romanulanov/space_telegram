import requests
import os
import argparse
from urllib.parse import urlparse, unquote
from download_image_and_file_extension import dwnld_image, get_file_ext


SPACEX_URL = 'https://api.spacexdata.com/v5/launches/'


def fetch_spacex_last_launch(launch_id='5eb87ce4ffd86e000604b338'):
    response = requests.get('{}{}'.format(SPACEX_URL, launch_id))
    response.raise_for_status()
    image_list = response.json()["links"]["flickr"]['original']
    for image_num, image in enumerate(image_list):
        filename = os.path.join('{}{}{}{}'.format('images/', 'spacex', str(image_num), get_file_ext(image)))
        dwnld_image(image, filename)


def main():
    os.makedirs('images/', exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument('id', nargs='?')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)


if __name__ == '__main__':
    main()

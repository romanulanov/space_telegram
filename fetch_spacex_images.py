import requests
import os
import argparse
from urllib.parse import urlparse, unquote
from download_image_and_file_extension import *


SPACEX_URL = 'https://api.spacexdata.com/v5/launches/'


def fetch_spacex_last_launch(id=''):
    if not id:
        response = requests.get('{}{}'.format(SPACEX_URL, '5eb87ce4ffd86e000604b338'))
    else:
        response = requests.get('{}{}'.format(SPACEX_URL, id))
    response.raise_for_status()
    image_list = response.json()["links"]["flickr"]['original']
    for image_num, image in enumerate(image_list):
        filename = os.path.join('{}{}{}{}'.format('images/', 'spacex', str(image_num), file_ext(image)))
        dwnld_jpg(image, filename)


def main():
    if not os.path.exists('images/'):
        os.makedirs('images/')
    parser = argparse.ArgumentParser()
    parser.add_argument('id', nargs='?')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)


if __name__ == '__main__':
    main()

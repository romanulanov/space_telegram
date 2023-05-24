import requests
import os
import argparse
from download_image_and_file_extension_and_get_images import dwnld_image, get_file_ext


SPACEX_URL = 'https://api.spacexdata.com/v5/launches/'


def fetch_spacex_last_launch(launch_id='5eb87ce4ffd86e000604b338'):
    response = requests.get(f"{SPACEX_URL}{launch_id}")
    response.raise_for_status()
    images = response.json()["links"]["flickr"]['original']
    for image_num, image in enumerate(images):
        filename = os.path.join('{}{}{}{}'.format('images/', 'spacex', image_num, get_file_ext(image)))
        dwnld_image(image, filename)


def main():
    os.makedirs('images/', exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument('id', nargs='?')
    args = parser.parse_args()
    if args.id:
        fetch_spacex_last_launch(args.id)
    else:
        fetch_spacex_last_launch()


if __name__ == '__main__':
    main()

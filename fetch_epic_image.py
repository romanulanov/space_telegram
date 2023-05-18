import requests
import os
import datetime
from download_image_and_file_extension import *
from dotenv import load_dotenv


def fetch_epic(token):
    image_list = []
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', {'count': 10, 'api_key': token})
    response.raise_for_status()
    json_list = response.json()
    for image in json_list:
        date_image, name_image = datetime.datetime.fromisoformat(image["date"]), image['image']
        image_list.append('{}{}{}{}{}'.format('https://api.nasa.gov/EPIC/archive/natural/', str(date_image.strftime("%Y/%m/%d")), '/png/', name_image, '.png'))
    for image_num, image in enumerate(image_list):
        response = requests.get(image, {'api_key': token})
        filename = os.path.join('{}{}{}{}'.format('images/', 'nasa_epic_', str(image_num), file_ext(image)))
        dwnld_image(response.url, filename)


def main():
    if not os.path.exists('images/'):
        os.makedirs('images/')
    token = os.environ["APOD_TOKEN"]
    fetch_epic(token)


if __name__ == '__main__':
    main()

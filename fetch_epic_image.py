import requests
import os
import datetime
from download_image_and_file_extension_and_get_images import dwnld_image, get_file_ext
from dotenv import load_dotenv


def fetch_epic(token):
    images = []
    count = 10
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', {'count': count, 'api_key': token})
    response.raise_for_status()
    response = response.json()
    for image in response:
        date_image, name_image = datetime.datetime.fromisoformat(image["date"]), image['image']
        images.append('{}{}{}{}{}'.format('https://api.nasa.gov/EPIC/archive/natural/', date_image.strftime("%Y/%m/%d"), '/png/', name_image, '.png'))
    for image_num, image in enumerate(images):
        response = requests.get(image, {'api_key': token})
        response.raise_for_status()
        filename = os.path.join('{}{}{}{}'.format('images/', 'nasa_epic_', image_num, get_file_ext(image)))
        dwnld_image(response.url, filename)


def main():
    load_dotenv()
    os.makedirs('images/', exist_ok=True)
    token = os.environ['APOD_TOKEN']
    fetch_epic(token)


if __name__ == '__main__':
    main()

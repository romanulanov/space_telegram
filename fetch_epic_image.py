import argparse
import requests
import os
import datetime
from download_image_and_file_extension_and_get_images import dwnld_image, get_file_ext
from dotenv import load_dotenv


def fetch_epic(token, count, path):
    images = []
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', {'count': count, 'api_key': token})
    response.raise_for_status()
    response = response.json()
    for image in response:
        date_image, name_image = datetime.datetime.fromisoformat(image["date"]), image['image']
        images.append('{}{}{}{}{}'.format('https://api.nasa.gov/EPIC/archive/natural/', date_image.strftime("%Y/%m/%d"), '/png/', name_image, '.png'))
    for image_num, image in enumerate(images):
        response = requests.get(image, {'api_key': token})
        response.raise_for_status()
        filename = os.path.join('{}{}{}{}'.format(path, 'nasa_epic_', image_num, get_file_ext(image)))
        dwnld_image(response.url, filename)
        if image_num == count - 1:
            break
      

def main():
    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='images', help='Введите название папки (по умолчанию images)')
    parser.add_argument('--count', type=int, default=10, help='Введите количество фото, которое надо скачать (по умолчанию 10)')
    args = parser.parse_args()
    os.makedirs(args.path, exist_ok=True)
    fetch_epic(nasa_token, args.count, f"{args.path}{'/'}")


if __name__ == '__main__':
    main()

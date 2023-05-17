import requests
import os
import datetime
from download_jpg_and_file_extension import *
from dotenv import load_dotenv


def fetch_epic(token):
    jpeg_list = []
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', {'count': 10, 'api_key': token})
    response.raise_for_status()
    json_list = response.json()
    for jpeg in json_list:
        date_jpeg, name_jpeg = datetime.datetime.fromisoformat(jpeg["date"]), jpeg['image']
        jpeg_list.append('{}{}{}{}{}'.format('https://api.nasa.gov/EPIC/archive/natural/', str(date_jpeg.strftime("%Y/%m/%d")), '/png/', name_jpeg, '.png'))
    for jpeg_num, jpeg in enumerate(jpeg_list):
        response = requests.get(jpeg, {'api_key': token})
        filename = os.path.join('{}{}{}{}'.format('images/', 'nasa_epic_', str(jpeg_num), file_ext(jpeg)))
        dwnld_jpg(response.url, filename)


def main():
    if not os.path.exists('images/'):
        os.makedirs('images/')
    token = os.environ["APOD_TOKEN"]
    fetch_epic(token)


if __name__ == '__main__':
    main()

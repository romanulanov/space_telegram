import requests
import os
import telegram
from urllib.parse import urlparse, unquote


def get_images(path):
    images = []
    for address, dirs, files in os.walk(path):
        for name in files:
            images.append(os.path.join(address, name))
    return images


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_ext(url):
    url = urlparse(unquote(url))
    return os.path.splitext(url.path)[1]


def send_message(tg_token, chat_token, file):
    bot = telegram.Bot(token=tg_token)
    with open(file, 'rb') as image:
        bot.send_document(chat_id=chat_token, document=image)

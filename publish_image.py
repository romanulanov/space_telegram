import argparse
import os
import random 
from dotenv import load_dotenv
from utils import get_images, send_message



def publish_image(tg_token, chat_token, path, image_name):
    if not image_name:
        images = get_images(path)
        send_message(tg_token, chat_token, random.choice(images))
    else:
        send_message(tg_token, chat_token, '{}{}'.format(path, image_name))


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    chat_token = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default='images', help='Введите папку где лежат фотографии (по умолчанию images)')
    parser.add_argument('--image_name', default='', help='Введите название картинки (по умолчанию "")')
    args = parser.parse_args()
    publish_image(tg_token, chat_token, args.path, args.image_name)


if __name__ == '__main__':
    main()

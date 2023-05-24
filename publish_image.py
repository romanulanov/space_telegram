import argparse
import telegram
import os
from dotenv import load_dotenv
from random import randint
from download_image_and_file_extension_and_get_images import get_images, send_message



def publish_image(tg_token, chat_token, image_name=''):
    if not image_name:
        images = get_images()
        send_message(tg_token, chat_token, images[randint(0, len(images)-1)])
    else:
        send_message(tg_token, chat_token, '{}{}'.format('images/', image_name))


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    chat_token = os.environ["TG_CHAT_ID"]
    parser = argparse.ArgumentParser()
    parser.add_argument('image_name', nargs='?')
    args = parser.parse_args()
    publish_image(tg_token, chat_token, args.image_name)


if __name__ == '__main__':
    main()

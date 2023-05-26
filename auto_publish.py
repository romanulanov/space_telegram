import requests
import telegram
import os
import random
import logging
from time import sleep
from dotenv import load_dotenv
from time import sleep
from download_image_and_file_extension_and_get_images import get_images, send_message


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    chat_token = os.environ["TG_CHAT_ID"]
    rate = 4
    imagepaths = get_images()
    while True:
        try:
            for image in imagepaths:
                send_message(tg_token, chat_token, image)
                sleep(rate*3600)
            random.shuffle(imagepaths)
        except telegram.error.NetworkError:
            sleep(60)
            pass


if __name__ == '__main__':
    main()

import argparse
import telegram
import os
import random
import logging
from time import sleep
from dotenv import load_dotenv
from time import sleep
import sys
from download_image_and_file_extension_and_get_images import get_images, send_message


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rate', default=4, help='Введите частоту публикаций (по умолчанию стоит раз в 4 часа)')
    args = parser.parse_args()
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    chat_token = os.environ["TG_CHAT_ID"]
    imagepaths = get_images()
    while True:
        try:
            for image in imagepaths:
                send_message(tg_token, chat_token, image)
                sleep(args.rate*3600)
            random.shuffle(imagepaths)
        except telegram.error.NetworkError:
            logging.error('Ошибка сети. Попробую переподключиться через минуту.')
            eprint(sys.stderr)
            sleep(60)            
            pass


if __name__ == '__main__':
    main()

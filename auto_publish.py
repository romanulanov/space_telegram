import telegram
import os
import random
from dotenv import load_dotenv
from time import sleep
from download_image_and_file_extension_and_get_images import get_images


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    chat_token = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=tg_token)
    rate = os.environ["RATE"]
    images = get_images()
    while True:
        for image in images:
            with open(image, 'rb') as image:
                bot.send_document(chat_id=chat_token, document=image)
            sleep(int(rate)*3600)
        random.shuffle(images)


if __name__ == '__main__':
    main()

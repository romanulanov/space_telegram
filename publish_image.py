import argparse
import telegram
import os
from dotenv import load_dotenv
from random import randint
from download_image_and_file_extension_and_get_images import get_images



def publish_image(tg_token, chat_token, image_name=''):
    bot = telegram.Bot(token=tg_token)
    if not image_name:
        images = get_images()
        with open(images[randint(0, len(images)-1)], 'rb') as image:
            bot.send_document(chat_id=chat_token, document=image)
    else:
        with open('{}{}'.format('images/', image_name), 'rb') as image:
            bot.send_document(chat_id=chat_token, document=image)



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

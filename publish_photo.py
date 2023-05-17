import argparse
import telegram
import os
from dotenv import load_dotenv
from random import randint


def publish_photo(tg_token, image_name=''):
    image_list = []
    bot = telegram.Bot(token=tg_token)
    if not image_name:
        for address, dirs, files in os.walk("images/"):
            for name in files:
                image_list.append(os.path.join(address, name))
        bot.send_document(chat_id='@spacespacspace', document=open(image_list[randint(0, len(image_list)-1)], 'rb'))
    else:
        bot.send_document(chat_id='@spacespacspace', document=open('{}{}'.format('images/', image_name), 'rb'))


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    parser = argparse.ArgumentParser()
    parser.add_argument('image_name', nargs='?')
    args = parser.parse_args()
    publish_photo(tg_token, args.image_name)


if __name__ == '__main__':
    main()

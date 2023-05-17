import telegram
import os
import random
from dotenv import load_dotenv
from time import sleep


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    bot = telegram.Bot(token=tg_token)
    rate = os.environ["RATE"]
    image_list = []
    for address, dirs, files in os.walk("images/"):
        for name in files:
            image_list.append(os.path.join(address, name))
    while True:
        for image in image_list:
            bot.send_document(chat_id='@spacespacspace', document=open(image, 'rb'))
            sleep(int(rate)*3600)
        random.shuffle(image_list)


if __name__ == '__main__':
    main()

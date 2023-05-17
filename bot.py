import telegram
import os
from dotenv import load_dotenv

load_dotenv()
tg_token = os.environ["TG_TOKEN"]
bot = telegram.Bot(token=tg_token)
bot.send_document(chat_id='@spacespacspace', document=open('images/nasa_apod_0.jpg', 'rb'))

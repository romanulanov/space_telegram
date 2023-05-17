import telegram
import os
from dotenv import load_dotenv

load_dotenv()
tg_token = os.environ["TG_TOKEN"]
bot = telegram.Bot(token=tg_token)


updates = bot.get_updates()
bot.send_message(chat_id='@spacespacspace', text="Проверка связи!")
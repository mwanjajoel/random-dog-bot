# import the libraries
from telegram.ext import Updater, CommandHandler
import requests
import re
import os
import logging
from dotenv import load_dotenv
load_dotenv()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# access the API and get the image URL
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']

    return image_url

# function to return the image to the sender 
def bop(update, context):
    url = get_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(os.getenv('BOT_TOKEN'), use_context=True)

    updater.start_webhook(listen="0.0.0.0", port=os.getenv('PORT'), url_path=os.getenv('BOT_TOKEN'))
    updater.bot.set_webhook(os.getenv('HEROKU_APP_NAME') + os.getenv('BOT_TOKEN'))
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




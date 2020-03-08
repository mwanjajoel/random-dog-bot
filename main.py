# import the libraries
from telegram.ext import Updater, CommandHandler
import requests
import re
from dotenv import load_dotenv
load_dotenv()

# access the API and get the image URL
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']

    return image_url

# function to return the image to the sender 
def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(os.getenv('BOT_TOKEN'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()




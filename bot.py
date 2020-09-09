from telegram.ext.dispatcher import run_async
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,ConversationHandler,CallbackQueryHandler
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import os
import unshortenit
from unshortenit import UnshortenIt
import pyshorteners
import re



Api_key=os.environ.get("api_key","")
s=pyshorteners.Shortener(api_key=Api_key)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

@run_async
def start(update,context):
    first=update.message.chat.first_name
    update.message.reply_text('Hi! '+str(first)+' \n\nWelcome to Url Expert Bot.\nThis bot can short long urls , and also unshort various short urls type /help to know how to use this bot.')

@run_async   
def help(update,context):
    update.message.reply_text('Just send the url that you want to short or unshort\n\nNote:<i>⚠️ Url must start with http:// or https:// and it should not have spaces in it.</i>',parse_mode=telegram.ParseMode.HTML)

@run_async
def convert(update,context):
    global link
    link=update.message.text
    pattern1="https://*"
    pattern2="http://*"
    if(re.search(pattern1,link)) or (re.search(pattern2,link)):
        keyboard = [[InlineKeyboardButton("Short", callback_data='short'),InlineKeyboardButton("Unshort", callback_data='unshort')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Select from below options whether you want to short or unshort your url', reply_markup=reply_markup)
    else:
        update.message.reply_text("<i>⚠️ Url must start with http:// or https:// and it should not have spaces in it.</i>",parse_mode=telegram.ParseMode.HTML)

@run_async
def button(update,context):
    query=update.callback_query
    query.answer()
    a=query.data
    if a=="unshort":
        unshortener=UnshortenIt()
        uri=unshortener.unshorten(link)
        query.edit_message_text(text="Unshorted url 👇🏼 : \n"+str(uri))
    if a=="short":
        response=s.bitly.short(link)
        query.edit_message_text("Shorted url 👇🏼:\n"+str(response))
		
def donate(update,context):
    update.message.reply_text("You can support me by donating any amount you wish by using the following *Payment Options* \n\n1\. [Paypal](https://paypal.me/yamit11) \n2\. UPI : `amity11@kotak` \n3\. [Debit/Credit cards/UPI](https://rzp.io/l/amity11)\n\n",parse_mode=telegram.ParseMode.MARKDOWN_V2)
	

	


def main():
    token=os.environ.get("bot_token","")
    updater = Updater(token,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler ('help',help))
    dp.add_handler(MessageHandler(Filters.text,convert))
    dp.add_handler(CommandHandler ('donate',donate))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

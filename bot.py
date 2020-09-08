from telegram.ext.dispatcher import run_async
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,ConversationHandler
import telegram
import logging
import os
import unshortenit
from unshortenit import UnshortenIt
import pyshorteners
shorts=range(1)
urls=range(1)


Api_key=os.environ.get("api_key","")
s=pyshorteners.Shortener(api_key=Api_key)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)





@run_async
def start(update,context):
    first=update.message.chat.first_name
    update.message.reply_text('Hi! '+str(first)+' \n\nWelcome to Link Expert 🔗 Bot.\nI can short long urls , and also unshort various short urls type /help to know how to use this bot.')

@run_async   
def help(update,context):
	update.message.reply_text('If you want to short your long url click /short and then send your long url\nIf you want to unshort the short url click /unshort and then send your short url')

@run_async   
def unshort(update,context):
	update.message.reply_text("send link that you want to unshort \n\n<i>⚠️ Url must start with http:// or https:// and it should not have spaces in it.</i>",parse_mode=telegram.ParseMode.HTML)
	return urls

@run_async
def short(update,context):
	update.message.reply_text("send url that you want to short \n\n<i>⚠️ Url must start with http:// or https:// and it should not have spaces in it.</i>",parse_mode=telegram.ParseMode.HTML)
	return shorts
	
def short_url(update,context):
	longurl=update.message.text
	if longurl=='/start':
		start(update,context)
		return ConversationHandler.END
	
	elif longurl=='/help':
		help(update,context)
		return ConversationHandler.END

	elif longurl=='/cancel':
		cancel (update,context)
		return ConversationHandler.END
		
	elif longurl=='/donate':
		donate (update,context)
		return ConversationHandler.END
	
	else:
		response=s.bitly.short(longurl)
		chat_id=update.message.chat_id
		context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
		update.message.reply_text("Shorted url is:\n"+str(response))
		return ConversationHandler.END
	
def url(update,context):
	url=update.message.text
	if url=='/start':
		start(update,context)
		return ConversationHandler.END
	elif url=='/help':
		help(update,context)
		return ConversationHandler.END
	elif url=='/cancel':
		cancel (update,context)
		return ConversationHandler.END
		
	elif url=='/donate':
		donate (update,context)
		return ConversationHandler.END
	else:
		unshortener=UnshortenIt()
		uri=unshortener.unshorten(url)
		chat_id=update.message.chat_id
		context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
		update.message.reply_text("Unshorted url is : \n"+str(uri))
		return ConversationHandler.END

	
def cancel(update, context):
	update.message.reply_text('Current Operation cancelled')
	return ConversationHandler.END

def donate(update,context):
	update.message.reply_text("You can support me by donating any amount you wish by using the following *Payment Options* \n\n1\. [Paypal](https://paypal.me/yamit11) \n2\. UPI : `amity11@kotak` \n3\. [Debit/Credit cards/UPI](https://rzp.io/l/amity11)\n\n",parse_mode=telegram.ParseMode.MARKDOWN_V2)
	

	


def main():
	token=os.environ.get("bot_token","")
	updater = Updater(token, use_context=True)
	dp = updater.dispatcher
	conv_handler1 = ConversationHandler(entry_points=[CommandHandler('short', short)],states={shorts:[MessageHandler(Filters.text,short_url)]},fallbacks=[CommandHandler('cancel', cancel)],allow_reentry=True)
	conv_handler = ConversationHandler(entry_points=[CommandHandler('unshort', unshort)],

        states={
            urls: [MessageHandler(Filters.text, url)],
           

        },

        fallbacks=[CommandHandler('cancel', cancel)],
        allow_reentry=True
    )
    
    
    
    

	dp.add_handler(conv_handler)
	dp.add_handler(conv_handler1)
	dp.add_handler(CommandHandler('start',start))
	dp.add_handler(CommandHandler ('short',list))
	dp.add_handler(CommandHandler ('help',help))
	dp.add_handler(CommandHandler ('donate',donate))
	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
    main()

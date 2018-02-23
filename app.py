import os


from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown


BOT_TOKEN = os.environ.get('BOT_TOKEN') # remember we set this earlier :)
APP_NAME = os.environ.get('HEROKU_APP_NAME') # remember we set this earlier :)
BOT_NAME = "@blahblahblah"
BOT_NAME_ESCAPED = escape_markdown(BOT_NAME)

PORT = int(os.environ.get('PORT', '80')) # this is set by heroku

WEBHOOK_PATH = "hook{}".format(TOKEN)
WEBHOOK_URL ="https://{}.herokuapp.com/{}".format(APP_NAME, WEBHOOK_PATH)

def start(bot, update):
    user_name = update.effective_user.name
    update.message.reply_text('Hello *{}*!'.format(escape_markdown(user_name)))


def help(bot, update):
    update.message.reply_text('this is the list of commands i support!!! \n...')


def handleTextMessage(bot, update):

	text = update.message.text
    
	
	if(if "hello" in text.lower()){
		print("daww user is trying to say hello to me!!!")
		
		reply = "HELLO THERE! MY NAME IS *{}*".format(BOT_NAME_ESCAPED)
		update.message.reply_text(reply, parse_mode="Markdown")
	}
	
	"""
	else if(text == "something else"){
		dosomethingelse!!!!
	}
	
	"""
	
	else {
		update.message.reply_text(text)
	}
	

def init():

	updater = Updater(BOT_TOKEN)

	updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=WEBHOOK_PATH)

	updater.bot.set_webhook(WEBHOOK_URL)

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start ))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(MessageHandler(Filters.text, handleTextMessage))

	updater.idle()


if __name__ == '__main__':

	init()
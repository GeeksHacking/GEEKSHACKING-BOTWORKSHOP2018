import os


from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

TOKEN = "400458894:AAHBO9dzUTASfEWZEbOB0oaN3k1wLVg2niM" # BOT TOKEN - should be in env var
APP_NAME = "geekhacking" ## heroku app name

PORT = int(os.environ.get('PORT', '80')) 
WEBHOOK_PATH = "hook{}".format(TOKEN)
WEBHOOK_URL ="https://{}.herokuapp.com/{}".format(APP_NAME, WEBHOOK_PATH)


def start(bot, update):
    user_name = update.effective_user.name
    update.message.reply_text('Hello *{}*!'.format(escape_markdown(user_name)))


def help(bot, update):
    update.message.reply_text('this is the list of commands i support!!! \n...')


def handleTextMessage(bot, update):
    update.message.reply_text(update.message.text)

def init():

	updater = Updater(TOKEN)

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
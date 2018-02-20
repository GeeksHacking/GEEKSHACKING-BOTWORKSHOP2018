import os


from telegram.ext import Updater

TOKEN = "400458894:AAHBO9dzUTASfEWZEbOB0oaN3k1wLVg2niM"
PORT = int(os.environ.get('PORT', '80'))
APP_NAME = "geekhacking"
WEBHOOK_PATH = "hook{}".format(TOKEN)
WEBHOOK_URL ="https://{}.herokuapp.com/{}".format(APP_NAME, WEBHOOK_PATH)


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    user_name = update.effective_user.name
    update.message.reply_text('Hello *{}*!'.format(escape_markdown(user_name))
				,parse_mode=True)


def help(bot, update):
    update.message.reply_text('this is the list of commands i support!!! \n...')


def message(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def main():

	updater = Updater(TOKEN)

	updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=WEBHOOK_PATH)

	updater.bot.set_webhook(WEBHOOK_URL)

	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start ))
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(MessageHandler(Filters.text, echo))

	# log all errors
	dp.add_error_handler(error)
	updater.idle()


if __name__ == '__main__':
	main()
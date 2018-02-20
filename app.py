import os


TOKEN = "400458894:AAHBO9dzUTASfEWZEbOB0oaN3k1wLVg2niM"
PORT = int(os.environ.get('PORT', '80'))
APP_NAME = "geekhacking"
WEBHOOK_PATH = "hook{}".format(TOKEN)
WEBHOOK_URL ="https://{}.herokuapp.com/{}".format(APP_NAME, WEBHOOK_PATH)

updater = Updater(TOKEN)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=WEBHOOK_PATH)

updater.bot.set_webhook(WEBHOOK_URL)
updater.idle()
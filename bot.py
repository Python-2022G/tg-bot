from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update

TOKEN = '6203711973:AAGQ0KgDqOiko9KnQZOF1i8hIluAuCuBWDk'

updater = Updater(token=TOKEN)

dp = updater.dispatcher


def start(update: Update, context: CallbackContext):
    update.message.reply_text(text="Salom, hush kelibsiz!")

def echo(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(text=text)


dp.add_handler(handler=CommandHandler('start', start))
dp.add_handler(handler=MessageHandler(filters=Filters.text, callback=echo))

updater.start_polling()
updater.idle()

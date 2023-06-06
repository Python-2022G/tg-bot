from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update

TOKEN = '6203711973:AAGQ0KgDqOiko9KnQZOF1i8hIluAuCuBWDk'

updater = Updater(token=TOKEN)


dp = updater.dispatcher


def start(update: Update, context: CallbackContext):
    chat = update.message.chat.id
    context.bot.sendMessage(chat, 'salom xush kelipsiz!')

def echo(update: Update, context: CallbackContext):
    chatid = update.message.chat.id
    text = update.message.text

    context.bot.sendMessage(chatid, text)


dp.add_handler(handler=CommandHandler('start', start))
dp.add_handler(handler=MessageHandler(filters=Filters.text, callback=echo))

updater.start_polling()
updater.idle()

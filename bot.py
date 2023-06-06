import telegram

TOKEN = '6203711973:AAGQ0KgDqOiko9KnQZOF1i8hIluAuCuBWDk'

bot = telegram.Bot(token=TOKEN)

# bot.send_message(chat_id='1258594598', text='hi')

updates = bot.getUpdates()

last_updates = updates[-1]

print(last_updates.update_id, last_updates.message.text)
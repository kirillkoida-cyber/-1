
import telebot

TOKEN = 8984563168:AAF8ztPmans_069719ih-E953klJDPtZgAg

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привіт! Бот працює! ✅")

bot.infinity_polling()

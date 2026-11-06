import logging
import os

import telebot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "Не задано змінну середовища BOT_TOKEN. "
        "Додай токен бота в налаштуваннях хостингу."
    )

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привіт! Бот працює! ✅")


if __name__ == "__main__":
    logging.info("Telegram-бот запускається...")
    bot.infinity_polling(skip_pending=True, timeout=30, long_polling_timeout=30)

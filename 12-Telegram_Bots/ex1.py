import telebot

import bot_secrets

import logging

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(bot_secrets.TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message: telebot.types.Message):
    logger.info(f"- starting from {message.chat.username}: {message.json}")
    bot.reply_to(message, "Welcome to this amazing bot!!!!\nPlease say something")


@bot.message_handler(func=lambda m: True)
def echo_all(message: telebot.types.Message):
    logger.info(f"- got message: from {message.chat.username}, {message.text!r}")
    bot.reply_to(message, message.text.replace("7", "❤️"))


logger.info("* starting bot")
bot.infinity_polling()
logger.info("* goodbye!")
import telebot
import bot_secrets
import logging
from telebot import types

logging.basicConfig(
    format="[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(bot_secrets.TOKEN)

# Dictionary to store user counters
user_counters = {}

# Function to ensure user exists in the dictionary
def ensure_user_counter(user_id):
    if user_id not in user_counters:
        user_counters[user_id] = 0

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    ensure_user_counter(message.from_user.id)

    # Create inline keyboard with increment and reset buttons
    keyboard = types.InlineKeyboardMarkup()
    increment_button = types.InlineKeyboardButton("Increment by 1", callback_data="increment")
    reset_button = types.InlineKeyboardButton("Reset", callback_data="reset")

    keyboard.add(increment_button, reset_button)

    bot.reply_to(message, "Welcome to the counter bot! Use the buttons below or enter a number:", reply_markup=keyboard)

@bot.message_handler(commands=['reset'])
def reset(message: telebot.types.Message):
    user_counters[message.from_user.id] = 0
    bot.reply_to(message, "Total: 0")

@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
    user_id = call.from_user.id
    ensure_user_counter(user_id)

    if call.data == "increment":
        user_counters[user_id] += 1
        bot.answer_callback_query(call.id, "Incremented by 1!")
    elif call.data == "reset":
        user_counters[user_id] = 0
        bot.answer_callback_query(call.id, "Counter reset!")

    # Update the message with the current total
    bot.edit_message_text(f"Total: {user_counters[user_id]}", chat_id=call.message.chat.id, message_id=call.message.message_id)

@bot.message_handler(func=lambda m: m.text.isdigit())
def count(message: telebot.types.Message):
    ensure_user_counter(message.from_user.id)
    user_counters[message.from_user.id] += int(message.text)
    bot.reply_to(message, f"Total: {user_counters[message.from_user.id]}")

@bot.message_handler(func=lambda m: True)
def echo_all(message: telebot.types.Message):
    bot.reply_to(message, "Please enter a number or use /reset.")

logger.info("* starting bot")
bot.infinity_polling()
logger.info("* goodbye!")

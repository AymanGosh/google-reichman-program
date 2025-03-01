import telebot
import wikipediaapi
import re
from datetime import datetime

# Initialize bot with your token
TOKEN = '7711673892:AAHG_D1Kdy4r6WFBef4p7CtQLzxea683Ab4'
bot = telebot.TeleBot(TOKEN)

# Initialize Wikipedia API with a valid user agent
wiki = wikipediaapi.Wikipedia(user_agent="TelegramCelebrityAgeBot/1.0 (your_email@example.com)", language="en")

def get_age(name):
    """Fetch celebrity age from Wikipedia."""
    page = wiki.page(name)
    if not page.exists():
        return None

    match = re.search(r'born (\w+ \d{1,2}, \d{4})', page.text)
    if match:
        birth_date = datetime.strptime(match.group(1), "%B %d, %Y")
        age = datetime.today().year - birth_date.year
        return age
    return None

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Enter a celebrity name and I'll tell you their age!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    name = message.text
    age = get_age(name)

    if age:
        bot.reply_to(message, str(age))
    else:
        bot.reply_to(message, f"Sorry, I don't know any '{name}'.")

# Start the bot
bot.polling()

from types import NoneType

import telebot
from backend import start

bot = telebot.TeleBot('7292519409:AAHGdCEoAXpxf8js0fG9RpdlHh-fPNWPe4o')

@bot.message_handler(['start'])
def ask(message):
    bot.send_message(message.chat.id, text=f"Погоду в каком городе вам необоходимо узнать?")
    bot.register_next_step_handler(message,answer)

def answer(message):
    city = message.text
    try:
        bot.send_message(message.chat.id,start(city))
    except AttributeError as e:
        bot.send_message(message.chat.id,f"Это был не город, милорд..")
    except Exception as e:
        bot.send_message(message.chat.id, f"Прости, милорд, я не знаю почему появилась эта ошибка: {e}")
bot.infinity_polling()
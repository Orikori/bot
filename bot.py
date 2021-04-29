import pyowm
from pyowm.utils.config import get_default_config
import telebot

bot = telebot.TeleBot("1750857579:AAFiTDZh5-vs1qY3YdxsU-0WWs70li3NnoE")

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM("8f22e9ecfc8085a61d544cb3eaaa4c1f", config_dict)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']

    answer = "В городе " + message.text + " сейчас \"" + w.detailed_status.title() + "\"\n"
    answer += "Температура в районе " + str(round(temperature)) + "\n"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)

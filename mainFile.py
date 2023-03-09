import telebot
from telebot import types
import config

bot = telebot.TeleBot('5837663231:AAH-Q8E4aSOJfikSTzep2wJlaYOB2wVsYDY')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Я водитель")
    btn2 = types.KeyboardButton("Я пассажир")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
                         message.from_user), reply_markup=markup)


bot.polling(none_stop=True)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import apihelper
from calendarHandler import *
import telebot
from config import *
import time
import logging
import databaseHandler

users = [427107060]

apihelper.proxy = {
    'https': 'socks5h://{}:{}@{}:{}'.format(USER2, PASSWORD2, IP2, PORT2)
}

bot = telebot.TeleBot(TOKEN)


# обработка команды event
@bot.message_handler(func=lambda message: message.chat.id in users, commands=['event'])
def get_text_messages(message):
    try:
        msg = upcomingEvents()
        bot.send_message(message.from_user.id, msg, parse_mode='HTML')
        time.sleep(1)
    except Exception as e:
        logging.error("Exception occured: ", exc_info=True)
        bot.send_message(message.from_user.id, "Так, босс, щас обдумаем тут помаленьку и все оформим. "
                                               "Погоди чуток")
        time.sleep(5)
        msg = upcomingEvents()
        bot.send_message(message.from_user.id, msg, parse_mode='HTML')


# функция для добавления нового места, ну клево же!
@bot.message_handler(func=lambda message: message.chat.id in users, commands=['place'])
def get_text_messages(message):
    try:
        sent = bot.send_message(message.from_user.id, 'Напиши плз в формате <b>город</b> / <b>место</b> /'
                                                      '<b>краткое описание</b>  и я запомню это местечко!',
                                parse_mode='HTML')
        bot.register_next_step_handler(sent, twoStepWriterFile)
    except Exception as e:
        logging.error("Exception occured: ", exc_info=True)
        bot.send_message(message.from_user.id, "Так, босс, щас обдумаем тут помаленьку и все оформим. "
                                               "Погоди чуток")
        time.sleep(5)
        bot.register_next_step_handler(sent, twoStepWriterFile)


def twoStepWriterFile(message):
    with open(r"places.txt", "a") as file:
        file.write(message.text + "\n")
        bot.send_message(message.from_user.id, 'Все запомнил, босс!',
                         parse_mode='HTML')


# какие города есть в списке
@bot.message_handler(func=lambda message: message.chat.id in users, commands=['cities'])
def get_text_messages(message):
    try:
        msg = databaseHandler.checkCity()
        bot.send_message(message.from_user.id, msg, parse_mode='HTML')
        time.sleep(1)
    except Exception as e:
        pass


# сообщение для левых ребят
@bot.message_handler(func=lambda message: message.chat.id not in users, commands=['event'])
def get_text_messages(message):
    try:
        bot.send_message(message.from_user.id, "Приветики!"
                                               " Хороший денек сегодня, да?")
    except Exception as e:
        logging.error("Exception occured: ", exc_info=True)
        bot.send_message(message.from_user.id, "Приветики!"
                                               " Хороший денек сегодня, да?")


bot.infinity_polling(none_stop=True, interval=0, timeout=100)

# TODO: добавить добавление и удаление событий в боте

#! /usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import apihelper
from calendarHandler import *
import telebot
from config import *
import time
import logging

users = [427107060, 274293840, 209733147]

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
        bot.send_message(message.from_user.id, "Увы, что-то пошло не так. "
                                               "Попробуем через 20 секунд еще раз, подождите...")
        time.sleep(20)
        msg = upcomingEvents()
        bot.send_message(message.from_user.id, msg, parse_mode='HTML')


# сообщение для левых ребят
@bot.message_handler(func=lambda message: message.chat.id not in users, commands=['event'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Приветики!"
                                           " Хороший денек сегодня, да?")


bot.polling(none_stop=True, interval=10, timeout=100)

# TODO: добавить добавление и удаление событий в боте

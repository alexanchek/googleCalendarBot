#! /usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import apihelper
from calendarHandler import *
import telebot
from config import *

users = [427107060, 274293840]

# TODO: CHANGE USER AGENT TO 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
#  Chrome/56.0.2924.87 Safari/537.36' IN requests,utils.py
apihelper.proxy = {
    'https': 'socks5://{}:{}@{}:{}'.format(USER2, PASSWORD2, IP2, PORT2)
}

bot = telebot.TeleBot(TOKEN)


# обработка команды event
@bot.message_handler(func=lambda message: message.chat.id in users, commands=['event'])
def get_text_messages(message):
    msg = upcomingEvents()
    bot.send_message(message.from_user.id, msg, parse_mode='HTML')


bot.polling(none_stop=True, interval=0, timeout=100)

# TODO: добавить добавление и удаление событий в боте

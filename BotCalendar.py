#! /usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import apihelper
from calendarHandler import *
import telebot
from config import *

users = [427107060, 274293840]

apihelper.proxy = {
    'https': 'socks5://{}:{}@{}:{}'.format(USER, PASSWORD, IP, PORT)
}

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: message.chat.id in users, commands=['event'])
def get_text_messages(message):
    msg = upcomingEvents()
    bot.send_message(message.from_user.id, msg, parse_mode='HTML')


bot.polling(none_stop=True, interval=0, timeout=100)

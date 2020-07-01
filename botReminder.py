#! /usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import apihelper
from calendarHandler import *
import telebot
from config import *
import schedule
import time

users = [427107060]

apihelper.proxy = {
    'https': 'socks5h://{}:{}@{}:{}'.format(USER2, PASSWORD2, IP2, PORT2)
}

bot = telebot.TeleBot(TOKEN)


def job():
    try:
        msg = upcomingEvents()
        bot.send_message(427107060, msg, parse_mode='HTML')
    except Exception as e:
        print("Тут такое дело... Кароче, надоб посмотреть тебе, чо там у нас по плану")


# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("08:00").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

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

telebot.apihelper.READ_TIMEOUT = 5

bot = telebot.TeleBot(TOKEN, threaded=False)


def main():
    try:
        msg = upcomingEvents()
        bot.send_message(427107060, msg, parse_mode='HTML')
    except Exception as e:
        print("Тут такое дело... Кароче, надоб посмотреть тебе, чо там у нас по плану")

if __name__ == "__main__":
    main()

# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("08:15").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

# while True:
#    schedule.run_pending()
#    time.sleep(1)

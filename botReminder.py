#! /usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import apihelper
from calendarHandler import *
import telebot
from config import *
import schedule
import time

users = [427107060, 274293840]

apihelper.proxy = {
    'https': 'socks5h://{}:{}@{}:{}'.format(USER, PASSWORD, IP, PORT)
}

bot = telebot.TeleBot(TOKEN)

def job():
    msg = upcomingEvents()
    bot.send_message(427107060, msg, parse_mode='HTML')


#schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("08:00").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

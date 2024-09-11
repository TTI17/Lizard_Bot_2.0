# from database_config import *
# import logging
# import asyncio
from dispatcher import *
from content_types import *
import telebot
from config import bot
from test import *

if __name__ == '__main__':
    logger = telebot.logger
    # telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
    bot.polling(none_stop=True, interval=0)
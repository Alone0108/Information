# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:36:49 2023

@author: Noutbuk Savdosi
"""


import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5943474480:AAFrBDbkwxih6gamOVqb_QIl1aqBPNblVT8'
wikipedia.set_lang('eng')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom MalumotlarW Botiga Xush kelibsiz!")



@dp.message_handler()
async def sendwiki(message: types.Message):
   try:
        respond=wikipedia.summary(message.text)
        await message.answer(respond)
   except:
        await message.answer('Bunday malumot yuq')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
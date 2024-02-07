from aiogram import Dispatcher, Bot, F
import asyncio
from aiogram.types import Message, ContentType
import logging
from core.handlers.basic import get_start, get_photo
from input import ADMIN_ID, TOKEN
from aiogram.filters import Command
from aiogram.filters.base import Filter


async def start_bot(bot:Bot):
    await bot.send_message(ADMIN_ID, 'Бот запущен')

async def stop_bot(bot:Bot):
    await bot.send_message(ADMIN_ID, 'Бот остановлен')



async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN)
    db = Dispatcher()
    db.message.register(get_start, Command(commands=['start', 'run']))
    db.startup.register(start_bot)
    db.shutdown.register(stop_bot)
    db.message.register(get_photo, F.photo)
    try:
        await db.start_polling(bot)

    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
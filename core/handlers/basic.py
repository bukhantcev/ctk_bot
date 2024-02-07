from aiogram import Bot
from aiogram.types import Message, ContentType


async def get_start(message:Message, bot:Bot):
    await message.answer("Первый экран")

async def get_photo(message: Message, bot:Bot):
    await message.answer(text='Photo')
import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from keyboards.main import catalog_menu, back_menu

basic_router = Router()

@basic_router.message(F.text == "Каталог")
async def catalog_callback(message: Message):
    await message.delete()

    await message.answer(
        "<b>Выберите категорию товара:</b>", 
        reply_markup=catalog_menu()
    )
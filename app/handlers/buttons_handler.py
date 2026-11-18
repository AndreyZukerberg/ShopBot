import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from keyboards.main import catalog_menu, back_menu, main_menu

basic_router = Router()

@basic_router.message(F.text == "Каталог")
async def catalog_callback(message: Message):
    await message.delete()

    await message.answer(
        "<b>Выберите категорию товара:</b>", 
        reply_markup=catalog_menu()
    )

@basic_router.message(F.text == "Контакты")
async def contacts_callback(message: Message):
    await message.delete()

    await message.answer(
        "<b>Наши контакты:</b>\n\n"
        "улица Пушкина, дом Колотушкина\n"
        "Телефон: +7 (123) 456-78-90\n"
        "Email: info@marketbot.ru", reply_markup=back_menu())

@basic_router.message(F.text == "Назад")
async def back_callback(message: Message):
    await message.delete()

    await message.answer(
        "<b>Вы вернулись в главное меню.</b>", 
        reply_markup=main_menu()
    )
    
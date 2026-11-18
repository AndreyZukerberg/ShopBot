from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main import main_menu

start_router = Router()

@start_router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "<b>Привет!</b> \nЯ бот магазина \"Гараж\" и я помогу тебе определиться с выбором товара или подскажу где находятся наши магазины!", 
        reply_markup=main_menu()
        )
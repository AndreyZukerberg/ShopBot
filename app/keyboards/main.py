from aiogram.types import (
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    KeyboardButton
)

def main_menu():
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Каталог"),
                KeyboardButton(text="Контакты")
            ],
            [
                KeyboardButton(text="Задать вопрос")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True, 
        is_persistent=False
    )
    return reply_keyboard

def back_menu():
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Назад")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=True, 
        is_persistent=False
    )
    return reply_keyboard

def catalog_menu():
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Мотоциклы", callback_data="moto")],
        [InlineKeyboardButton(text="Квадроциклы", callback_data="quadro")],
        [InlineKeyboardButton(text="Генераторы", callback_data="generator")],
        [InlineKeyboardButton(text="Бензопилы", callback_data="chainsaw")],
        [InlineKeyboardButton(text="Инструменты", callback_data="tools")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]],
        resize_keyboard=True,
    )
    return inline_keyboard
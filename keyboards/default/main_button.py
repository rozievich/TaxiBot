from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Habar yuborish"), 
        KeyboardButton(text="Taxilar ro'yhati"), 
        KeyboardButton(text="Hozirda mavjuda taxilar")
    ]],
    one_time_keyboard=True,
    resize_keyboard=True
)
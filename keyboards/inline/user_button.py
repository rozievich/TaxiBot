from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import bot_link

button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="➕", url=bot_link)
    ]]
)

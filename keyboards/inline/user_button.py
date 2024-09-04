from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import BOT_LINK

button = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="➕", url=BOT_LINK)
    ]]
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚖 Taxi zakaz qilish", url="https://t.me/m39_taxi_bot?start=true")
        ],
        [
        InlineKeyboardButton(text="🚘 Haydovchi bo'lib ishlash", url="https://t.me/isakoMR")
        ]
    ]
)

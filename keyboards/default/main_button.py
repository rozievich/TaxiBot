from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="E'lon yuborish ✈️"),
        KeyboardButton(text="Barcha Taxilar 🚕"),
        KeyboardButton(text="Top Taxilar 🏆")
    ]],
    one_time_keyboard=True,
    resize_keyboard=True
)


admin_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Taxi Qo'shish 🚕"),
        KeyboardButton(text="Taxi O'chirish 🚖"),
        KeyboardButton(text="Statistika 📊")
    ]],
    one_time_keyboard=True,
    resize_keyboard=True,
)


exit_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="❌")
    ]],
    one_time_keyboard=True,
    resize_keyboard=True
)


exit_and_skip_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="❌"),
    ],
    [
        KeyboardButton(text="⛓ O'tkazib yuborish ⛓")
    ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True,
)

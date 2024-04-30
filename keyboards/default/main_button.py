from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="E'lon yuborish ✈️"),
        KeyboardButton(text="Barcha Taxilar 🚕")
    ],
    [
        KeyboardButton(text="Top Taxilar 🏆")
    ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)


admin_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Taxi Qo'shish 🚕"),
        KeyboardButton(text="Taxi O'chirish 🚖")
    ],
    [
        KeyboardButton(text="Statistika 📊")
    ],
    [
        KeyboardButton(text="Topga chiqarish 🏆"),
        KeyboardButton(text="Topdan chiqarish 🔙")
    ]
    ],
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


async def get_all_users_button(taxies: list):
    all_users = []
    for user in taxies:
        if user['fullname'] == taxies[-1]['fullname']:
            all_users.append([KeyboardButton(text=user['fullname'])])
            all_users.append([KeyboardButton(text="❌")])
        else:
            all_users.append([KeyboardButton(text=user['fullname'])])
    
    button = ReplyKeyboardMarkup(keyboard=all_users, one_time_keyboard=True, resize_keyboard=True)
    return button

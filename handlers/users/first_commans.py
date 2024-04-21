from aiogram import Bot, types
from keyboards.default.main_button import start_button, admin_button
from data.config import ADMINS


async def start_command(message: types.Message, bot: Bot):
    if message.chat.type == "private":
        await bot.set_my_commands([types.BotCommand(command='start', description="Botni ishga tushirish ♻️"), types.BotCommand(command='help', description="Yordam olish 🆘")])
        await message.answer(f"Assalomu alaykum {message.from_user.full_name} 👋\nTaxi botga xush kelibsiz 🚕\nPastdan kerakli bo'limni tanlang 🔗", reply_markup=start_button)
    else:
        await message.answer("Assalomu alaykum 👋\nTaxi topish botiga xush kelibsiz 🚕\nEndi murojaat qilingan guruhda men hech narsa qilolmayman 😔\n Shaxsiy xabar yuboring va biz boshlaymiz 🤖")



async def help_command(message: types.Message):
    await message.answer("Botdan foydalanish haqida qisqacha")


async def panel_command(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer(f"{message.from_user.full_name} admin sahifaga xush kelibsiz 🤖\nIltimos kerakli bo'limni tanlang 🎛", reply_markup=admin_button)


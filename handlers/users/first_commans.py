from aiogram import Bot, types, Router
from aiogram.filters import CommandStart, Command

from keyboards.default.main_button import start_button, admin_button
from main import db
from data.config import ADMINS


users_router = Router()


@users_router.message(CommandStart())
async def start_command(message: types.Message, bot: Bot):
    if message.chat.type == "private":
        user = db.get_user(user_id=str(message.from_user.id))
        if not user:
            db.create_user(user_id=str(message.from_user.id))
        await bot.set_my_commands([types.BotCommand(command='start', description="Botni ishga tushirish ♻️"), types.BotCommand(command='help', description="Yordam olish 🆘")])
        await message.answer(f"Assalomu alaykum {message.from_user.full_name} 👋\nTaxi botga xush kelibsiz 🚕\nPastdan kerakli bo'limni tanlang 🔗", reply_markup=start_button)
    else:
        await message.answer("Assalomu alaykum 👋\nTaxi topish botiga xush kelibsiz 🚕\nEndi murojaat qilingan guruhda men hech narsa qilolmayman 😔\nShaxsiy xabar yuboring va biz boshlaymiz 🤖")


@users_router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("Botdan foydalanish haqida qisqacha")


@users_router.message(Command('panel'))
async def panel_command(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer(f"{message.from_user.full_name} admin sahifaga xush kelibsiz 🤖\nIltimos kerakli bo'limni tanlang 🎛", reply_markup=admin_button)

from aiogram import Bot, types
from keyboards.default.main_button import start_button


async def start_command(message: types.Message, bot: Bot):
    await bot.set_my_commands([types.BotCommand(command='start', description="Botni ishga tushirish ♻️"), types.BotCommand(command='help', description="Yordam olish 🆘"), types.BotCommand(command="profile", description="Mening profilim 👤")])
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} 👋\nBotga xush kelibsiz\n", reply_markup=start_button)


async def help_command(message: types.Message):
    await message.answer("Botdan foydalanish haqida qisqacha")



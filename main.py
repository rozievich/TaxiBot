import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from data.config import TOKEN
from handlers.first_commans import mainrouter
from keyboards.inline.user_button import button
from utils.db_api.connect import start_up
from utils.db_api.orm import TaxiDB


dp = Dispatcher(storage=MemoryStorage())
db = TaxiDB()


async def member_joined(message: types.Message):
    if message.new_chat_members:
        new_member = message.new_chat_members[0]
        await message.reply(
            f"Assalomu alaykum {new_member.full_name} 🤖\n"
            f"Bizning bot orqali tez va oson taxi toping ✅\n\n"
            f"Pastdagi ➕ tugmasini bosing va foydalanishni boshlang 🎛",
            reply_markup=button
        )


async def main() -> None:
    dp.message.register(member_joined, F.new_chat_member)
    dp.include_routers(
        mainrouter
    )
    dp.startup.register(start_up)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

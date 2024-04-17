import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from data.config import TOKEN
from handlers.users import user_router
from utils.db_api.connect import start_up

dp = Dispatcher()


async def main() -> None:
    dp.include_routers(
        user_router
    )
    dp.startup.register(start_up)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
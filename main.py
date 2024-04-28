import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

import handlers, filters, states, utils
from data.config import TOKEN
# from handlers.users import users_router
from handlers.admin import admin_router
from utils.db_api.connect import start_up
from utils.db_api.orm import TaxiDB

dp = Dispatcher(storage=MemoryStorage())
db = TaxiDB()


async def main() -> None:
    dp.include_routers(
        # users_router,
        admin_router
    )
    dp.startup.register(start_up)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

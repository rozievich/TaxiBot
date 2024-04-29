from aiogram import types

from .first_commans import mainrouter
from data.config import ADMINS
from utils.db_api.orm import TaxiDB

db = TaxiDB()

@mainrouter.message(lambda msg: msg.text == "Statistika 📊")
async def get_user_statistic(message: types.Message):
    if message.from_user.id in ADMINS:
        all_users = db.get_users()
        await message.answer(f"Bot foydalanuvchilari soni: <b>{len(all_users)}</b>")

from aiogram import types
from aiogram.fsm.context import FSMContext

from main import db
from .first_commans import mainrouter



@mainrouter.message(lambda msg: msg.text == "Barcha Taxilar 🚕")
async def all_taxi_get_func(message: types.Message):
    all_taxi = db.get_taxies()
    for i in all_taxi:
        await message.answer_photo(photo=i['photo'], caption=f"Taxi haqida ma'lumot ℹ️\n\nIsm - Familiya: <b>{i['fullname']}\nTelefon: <b>{i['phone']}</b>\nBatafsil ma'lumot: {i['description']}", reply_markup=)


from aiogram import types
from aiogram.fsm.context import FSMContext

from main import db
from .first_commans import mainrouter



@mainrouter.message(lambda msg: msg.text == "Barcha Taxilar 🚕")
async def all_taxi_get_func(message: types.Message):
    all_taxi = db.get_taxies()
    for i in all_taxi:
        if not i['username']:
            await message.answer_photo(photo=i['photo'], caption=f"Taxi haqida ma'lumot ℹ️\n\nIsm - Familiya: <b>{i['fullname']}\nTelefon: <b>{i['phone']}</b>\nBatafsil ma'lumot: {i['description']}")
        else:
            await message.answer_photo(photo=i['photo'], caption=f"Taxi haqida ma'lumot ℹ️\n\nIsm - Familiya: <b>{i['fullname']}\nTelefon: <b>{i['phone']}</b>\nBatafsil ma'lumot: {i['description']}\n\n <a href='https://t.me/{i['username'][1:]}/'>📞 Bog'lanish uchun 📞</a>")


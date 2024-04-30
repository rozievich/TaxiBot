from aiogram import types

from main import db
from .first_commans import mainrouter



@mainrouter.message(lambda msg: msg.text == "Barcha Taxilar 🚕")
async def all_taxi_get_func(message: types.Message):
    all_taxi = db.get_taxies()
    if all_taxi:
        for i in all_taxi:
            if not i['username']:
                await message.answer_photo(photo=i['photo'], caption=f"Taxi haqida ma'lumot ℹ️\n\nIsm - Familiya: <b>{i['fullname']}\nTelefon: <b>{i['phone']}</b>\nBatafsil ma'lumot: {i['description']}")
            else:
                await message.answer_photo(photo=i['photo'], caption=f"Taxi haqida ma'lumot ℹ️\n\nIsm - Familiya: <b>{i['fullname']}\nTelefon: <b>{i['phone']}</b>\nBatafsil ma'lumot: {i['description']}\n\n <a href='https://t.me/{i['username'][1:]}/'>📞 Bog'lanish uchun 📞</a>")
    else:
        await message.answer("Kechirasiz hozircha Taxilar mavjud emas 🛑")


@mainrouter.message(lambda msg: msg.text == "Top Taxilar 🏆")
async def get_top_taxi_func(message: types.Message):
    all_top_taxi = db.get_top_taxi()
    if all_top_taxi:
        for taxi in all_top_taxi:
            if not taxi['username']:
                await message.answer_photo(photo=taxi['photo'], caption=f"Taxi haqida ma'lumot ℹ️\n\nIsm - Familiya: <b>{taxi['fullname']}\nTelefon: <b>{taxi['phone']}</b>\nBatafsil ma'lumot: {taxi['description']}")
            else:
                await message.answer_photo(photo=taxi['photo'], caption=f"Taxi haqida ma'lumot ℹ️\n\nIsm - Familiya: <b>{taxi['fullname']}\nTelefon: <b>{taxi['phone']}</b>\nBatafsil ma'lumot: {taxi['description']}\n\n <a href='https://t.me/{taxi['username'][1:]}/'>📞 Bog'lanish uchun 📞</a>")
    else:
        await message.answer("Kechirasiz hozircha top Taxilar mavjud emas 🛑")

from aiogram import types
from aiogram.fsm.context import FSMContext

from data.config import ADMINS
from keyboards.default.main_button import admin_button, get_all_top_taxis
from states.admin_states import UpdateTopState, UpdateBackTopState
from utils.db_api.orm import TaxiDB
from .first_commans import mainrouter

db = TaxiDB()



@mainrouter.message(lambda msg: msg.text == "Topga chiqarish 🏆")
async def update_top_taxi_func(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        users = db.get_taxies()
        if users:
            await message.answer("Topga chiqarish kerak bo'lgan taxini tanlang 🏆", reply_markup=await get_all_top_taxis(users, False))
            await state.set_state(UpdateTopState.fullname)
        else:
            await message.answer("Hozirda tizimda hech qanday taxi yo'q 🛑")


@mainrouter.message(UpdateTopState.fullname)
async def update_top_taxi_fullname(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            user_info = db.get_taxi(message.text)
            if user_info:
                db.update_top_taxi(_id=user_info['id'], top=True)
                await message.answer(f"{message.text} - endi top ro'yhatida 🏆", reply_markup=admin_button)
                await state.clear()
            else:
                await message.answer("Bunday user tizimda ro'yhatdan o'tmagan 🤷‍♂️\nIltimos qayta urunib ko'ring 🤖", reply_markup=admin_button)
                await state.clear()


@mainrouter.message(lambda msg: msg.text == "Topdan chiqarish 🔙")
async def update_top_taxi_func_false(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        users = db.get_taxies()
        if users:
            await message.answer("Topdan chiqarish kerak bo'lgan taxini tanlang 🏆", reply_markup=await get_all_top_taxis(users, True))
            await state.set_state(UpdateBackTopState.fullname)
        else:
            await message.answer("Hozirda tizimda hech qanday top taxi yo'q 🛑")
            

@mainrouter.message(UpdateBackTopState.fullname)
async def update_top_taxi_func_fullname_false(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            user_info = db.get_taxi(message.text)
            if user_info:
                db.update_top_taxi(_id=user_info['id'], top=False)
                await message.answer(f"{message.text} - endi top ro'yhatida emas 🏆", reply_markup=admin_button)
                await state.clear()
            else:
                await message.answer("Bunday user tizimda ro'yhatdan o'tmagan 🤷‍♂️\nIltimos qayta urunib ko'ring 🤖", reply_markup=admin_button)
                await state.clear()

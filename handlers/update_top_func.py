from aiogram import types
from aiogram.fsm.context import FSMContext

from data.config import ADMINS
from keyboards.default.main_button import admin_button, exit_button
from states.admin_states import UpdateTopState, UpdateBackTopState
from utils.db_api.orm import TaxiDB
from .add_taxi_func import taxirouter

db = TaxiDB()



@taxirouter.message(lambda msg: msg.text == "Topga chiqarish 🏆")
async def update_top_taxi_func(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Topga chiqarish kerak bo'lgan taxini tanlang 🏆", reply_markup=exit_button)
        await state.set_state(UpdateTopState.fullname)


@taxirouter.message(UpdateTopState.fullname)
async def update_top_taxi_fullname(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            user_info = db.get_taxi(message.text)
            if user_info:
                db.update_top_taxi(user_info['id'], True)
                await message.answer(f"{message.text} - endi top ro'yhatida 🏆")
                await state.clear()
            else:
                await message.answer("Bunday user tizimda ro'yhatdan o'tmagan 🤷‍♂️\nIltimos qayta urunib ko'ring 🤖", reply_markup=admin_button)
                await state.clear()


@taxirouter.message(lambda msg: msg.text == "Topdan chiqarish 🔙")
async def update_top_taxi_func_false(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Topdan chiqarish kerak bo'lgan taxini tanlang 🏆", reply_markup=exit_button)
        await state.set_state(UpdateBackTopState.fullname)
    

@taxirouter.message(UpdateBackTopState.fullname)
async def update_top_taxi_func_fullname_false(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            user_info = db.get_taxi(message.text)
            if user_info:
                db.update_top_taxi(user_info['id'], False)
                await message.answer(f"{message.text} - endi top ro'yhatida emas 🏆")
                await state.clear()
            else:
                await message.answer("Bunday user tizimda ro'yhatdan o'tmagan 🤷‍♂️\nIltimos qayta urunib ko'ring 🤖", reply_markup=admin_button)
                await state.clear()

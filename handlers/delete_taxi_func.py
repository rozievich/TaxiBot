from aiogram import types
from aiogram.fsm.context import FSMContext

from data.config import ADMINS 
from states.admin_states import DeleteTaxiState
from keyboards.default.main_button import admin_button, get_all_users_button
from utils.db_api.orm import TaxiDB
from .first_commans import mainrouter

db = TaxiDB()



@mainrouter.message(lambda msg: msg.text == "Taxi O'chirish 🚖")
async def delete_taxi_function_fullname(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        users = db.get_taxies()
        if users:
            print(users)
            await message.answer("O'chirish kerak bo'lgan Taxining Ism Familiyasini tanlang ⚙️", reply_markup=await get_all_users_button(users))
            await state.set_state(DeleteTaxiState.fullname)
        else:
            await message.answer("O'chirish uchun taxi topilmadi 🛑")
    

@mainrouter.message(DeleteTaxiState.fullname)
async def delete_taxi_function_finish(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            user_info = db.get_taxi(message.text)
            if user_info:
                db.delete_taxi(user_info['id'])
                await message.answer("Taxi muvaffaqiyatli o'chrildi ✅", reply_markup=admin_button)
                await state.clear()
            else:
                await message.answer("Bunday user tizimda ro'yhatdan o'tmagan 🤷‍♂️\nIltimos qayta urunib ko'ring 🤖", reply_markup=admin_button)
                await state.clear()

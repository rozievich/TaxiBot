from aiogram import types
from aiogram.fsm.context import FSMContext

from data.config import ADMINS 
from states.admin_states import DeleteTaxiState
from keyboards.default.main_button import admin_button 
from main import db



async def delete_taxi_function_fullname(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("O'chirish kerak bo'lgan Taxining Ism Familiyasini tanlang ⚙️", reply_markup=admin_button)
        await state.set_state(DeleteTaxiState.fullname)
    

async def delete_taxi_function_finish(message: types.Message, state: FSMContext):
    if message.from_user in ADMINS:
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

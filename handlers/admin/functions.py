from aiogram import types, Bot
from data.config import ADMINS
from states.admin_states import AddTaxiState
from aiogram.fsm.context import FSMContext


async def add_taxi_function(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Ism Familiyasini kiriting: ")
        await state.set_state(AddTaxiState.fullname)


async def add_taxi_function_phone(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(fullname=message.text)
        await message.answer("Telefon raqamni kiriting: ")
        await state.set_state(AddTaxiState.phone)


async def add_taxi_function_photo(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(phone=message.text)
        await message.answer("Rasm kiriting (Ixtiyoriy): ")
        await state.set_state(AddTaxiState.photo)


async def add_taxi_function_username(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(photo=message.photo.file_id)
        await message.answer("Taxining Telegram Usernameni kiriting: ")
        await state.set_state(AddTaxiState.username)


async def add_taxi_function_description(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(username=message.text)
        await message.answer("Taxi uchun izoh kiriting: ")
        await state.set_state(AddTaxiState.description)


async def add_taxi_function_finish(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        user_info = await state.get_data()
        await message.answer("Barchasi to'g'rimi")
        await state.clear()


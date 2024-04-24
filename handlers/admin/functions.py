import re
from aiogram import types, Bot
from data.config import ADMINS
from states.admin_states import AddTaxiState
from aiogram.fsm.context import FSMContext


async def add_taxi_function(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Taxining Ism Familiyasini kiriting 👤")
        await state.set_state(AddTaxiState.fullname)


async def add_taxi_function_phone(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await state.update_data(fullname=message.text)
        await message.answer("Taxining Telefon raqamini kiriting ✒️\nMisol uchun: +998901234567")
        await state.set_state(AddTaxiState.phone)


async def add_taxi_function_photo(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if re.match("^(\+998|998|0)?[1-9]\d{8}$", message.text):
            await state.update_data(phone=message.text)
            await message.answer("Taxining Rasmini kiriting (Ixtiyoriy) 📸")
            await state.set_state(AddTaxiState.photo)
        else:
            await message.answer("Iltimos telefon raqamni to'g'ri kiriting ⚠️\nMisol uchun: +998901234567")


async def add_taxi_function_username(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        try:
            await state.update_data(photo=message.photo.file_id)
            await message.answer("Taxining Telegram Usernameni kiriting 🔗")
            await state.set_state(AddTaxiState.username)
        except:
            await message.answer("Iltimos Rasm kiritayotganingizga ishonch hosil qiling 🚫")


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


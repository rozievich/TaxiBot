import re
from aiogram import types
from aiogram.fsm.context import FSMContext
from data.config import ADMINS, DEFAULT_IMAGE
from states.admin_states import AddTaxiState
from keyboards.default.main_button import exit_button, admin_button, exit_and_skip_button



async def add_taxi_function(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Taxining Ism Familiyasini kiriting 👤", reply_markup=exit_button)
        await state.set_state(AddTaxiState.fullname)


async def add_taxi_function_phone(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            await state.update_data(fullname=message.text)
            await message.answer("Taxining Telefon raqamini kiriting ✒️\nMisol uchun: +998901234567", reply_markup=exit_button)
            await state.set_state(AddTaxiState.phone)


async def add_taxi_function_photo(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            if re.match("^(\+998|998|0)?[1-9]\d{8}$", message.text):
                await state.update_data(phone=message.text)
                await message.answer("Taxining Rasmini kiriting (Ixtiyoriy) 📸", reply_markup=exit_and_skip_button)
                await state.set_state(AddTaxiState.photo)
            else:
                await message.answer("Iltimos telefon raqamni to'g'ri kiriting ⚠️\nMisol uchun: +998901234567")


async def add_taxi_function_username(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        elif message.text == "⛓ O'tkazib yuborish ⛓":
            await state.update_data(photo=DEFAULT_IMAGE)
            await message.answer("Taxining Telegram Usernameni kiriting (Ixtiyoriy) 🔗\nMisol uchun: <b>@username</b>", reply_markup=exit_and_skip_button)
            await state.set_state(AddTaxiState.username)
        else:
            try:
                await state.update_data(photo=message.photo.file_id)
                await message.answer("Taxining Telegram Usernameni kiriting (Ixtiyoriy) 🔗\nMisol uchun: <b>@username</b>", reply_markup=exit_and_skip_button)
                await state.set_state(AddTaxiState.username)
            except:
                await message.answer("Iltimos Rasm kiritayotganingizga ishonch hosil qiling 🚫")


async def add_taxi_function_description(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
            return
        elif message.text == "⛓ O'tkazib yuborish ⛓":
            await state.update_data(username="")
            await message.answer("Taxining xususiyatlarini kiriting (Ixtiyoriy) ⚙️", reply_markup=exit_and_skip_button)
            await state.set_state(AddTaxiState.description)
        else:
            if re.match("^@[A-Za-z0-9_]{5,32}$", message.text): 
                await state.update_data(username=message.text)
                await message.answer("Taxining xususiyatlarini kiriting (Ixtiyoriy) ⚙️", reply_markup=exit_and_skip_button)
                await state.set_state(AddTaxiState.description)
            else:
                await message.answer("Iltimos usernameni to'gri kiriting 🆘")



async def add_taxi_function_finish(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text == "❌":
            await message.answer("Jarayon tugatildi 🛑", reply_markup=admin_button)
            await state.clear()
        else:
            user_info = state.get_data()
            await message.answer_photo(photo=user_info['photo'], caption=f"<b>Ism Familiya:</b> {user_info['fullname']}\n\n<b>Ma'lumotlari:</b> {message.text}\n<b>Telefon:</b> {user_info['phone']}")
            await message.answer("Barchasi to'g'rimi")
        await state.clear()


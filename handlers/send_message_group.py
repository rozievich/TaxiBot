from aiogram import types, Bot
from aiogram.fsm.context import FSMContext

from states.users_states import SendMessageState
from data.config import TO_GROUP_ID
from keyboards.default.main_button import exit_button, start_button
from filters.admin_filter import TextFilter
from .first_commans import mainrouter
from data.config import ADMINS


@mainrouter.message(TextFilter("E'lon yuborish ✈️"))
async def send_message_func(message: types.Message, state: FSMContext):
    await message.answer("E'loningizni yozib qoldiring tez orada taxilar siz bilan bog'lanishadi 🚕\nEslatib o'tamiz bog'lanish uchun <b>telefon raqam</b> yoki <b>telegram username</b> yozib qoldiring 🔗", reply_markup=exit_button)
    await state.set_state(SendMessageState.text)


@mainrouter.message(SendMessageState.text)
async def send_message_func_finish(message: types.Message, bot: Bot, state: FSMContext):
    if message.text == "❌":
        await message.answer("E'lon yuborish bekor qilindi 🛑", reply_markup=start_button)
        await state.clear()
    else:
        await bot.send_message(chat_id=TO_GROUP_ID, text=message.text + f"\n\n<a href='https://t.me/{message.from_user.username}/'><b>Telegram</b></a>")
        await message.answer("E'loningiz muvaffaqiyatli yuborildi ✅", reply_markup=start_button)
        await state.clear()


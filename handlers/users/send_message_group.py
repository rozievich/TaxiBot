from aiogram import types, Bot
from aiogram.fsm.context import FSMContext

from states.user_states import SendMessageState
from data.config import TO_GROUP_ID
from keyboards.default.main_button import exit_button


async def send_message_func(message: types.Message, state: FSMContext):
    await message.answer("E'loningizni yozib qoldiring tez orada taxilar siz bilan bog'lanishadi 🚕\nEslatib o'tamiz bog'lanish uchun <b>telefon raqam</b> yoki <b>telegram username</b> yozib qoldiring 🔗", reply_markup=exit_button)
    await state.set_state(SendMessageState.text)


async def send_message_func_finish(message: types.Message, bot: Bot, state: FSMContext):
    user_text = message.text + f"\n\n{message.from_user.mention_html("📞 Bog'lanish uchun bosing 📞")}"
    await bot.send_message(chat_id=TO_GROUP_ID, text=user_text)
    await state.clear()

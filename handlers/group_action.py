from aiogram import Bot, types

from data.config import FROM_GROUP_ID, TO_GROUP_ID, KEYBOARDS
from .first_commans import mainrouter


async def forward_message_to_small_group(message: types.Message, bot: Bot):
    msg = message
    await message.delete()
    await bot.send_message(chat_id=TO_GROUP_ID, text=f"<b>Message:</b> {msg.text}\n\n<b>Ism:</b> {msg.from_user.mention_html(msg.from_user.full_name)}\n<b>Username:</b> {msg.from_user.username}\n<b>Guruh:</b> @{msg.chat.username}")
    await message.answer(f"ASSALOMU ALEYKUM #{msg.from_user.full_name}\nSIZNING ZAKAZINGIZ SHAFYORLAR 🚖 GURUHIGA TUSHDI ✅\nLICHKADA ISHONCHLI SHAFYORLARIMIZ KUTMOQDA❗️\n\nYOKI ADMINGA MUROJAT QILING:\n☎️ +998944403995\n☎️ +998994041819\n\nGRUPPA SIZGA MAQUL BO'LSA DO'STLARIZGA ULASHING.\n@Yaypan_Toshkent_Robot")

async def message_contains_keyword(message: str):
    if message:
        for keyword in KEYBOARDS:
            if keyword in message:
                return True
        return False
    else:
        return False


@mainrouter.message()
async def handle_big_group_messages(message: types.Message, bot: Bot):
    if message.chat.type == "supergroup" and message.chat.id in FROM_GROUP_ID:
        if await message_contains_keyword(message=message.text):
            await forward_message_to_small_group(message, bot)

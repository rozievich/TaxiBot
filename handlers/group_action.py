from aiogram import Bot, types

from data.config import FROM_GROUP_ID, TO_GROUP_ID, KEYBOARDS
from .first_commans import mainrouter


async def forward_message_to_small_group(msg: types.Message, bot: Bot):
    await bot.send_message(chat_id=TO_GROUP_ID, text=f"<b>Message:</b> {msg.text}\n\n<b>Ism:</b> {msg.from_user.mention_html(msg.from_user.full_name)}\n<b>Username:</b> {msg.from_user.username}\n<b>Guruh:</b> @{msg.chat.username}")
    await bot.send_message(chat_id=msg.chat.id, text=f"ASSALOMU ALEYKUM #{msg.from_user.full_name}\nSIZNING ZAKAZINGIZ SHAFYORLAR 🚖 GURUHIGA TUSHDI ✅\nLICHKADA ISHONCHLI SHAFYORLARIMIZ KUTMOQDA❗️\n\nYOKI ADMINGA MUROJAT QILING:\n☎️ +998944403995\n☎️ +998994041819\n\nGRUPPA SIZGA MAQUL BO'LSA DO'STLARIZGA ULASHING.\n@Yaypan_Toshkent_Robot")


@mainrouter.message()
async def handle_big_group_messages(message: types.Message, bot: Bot):
    if message.chat.type == "supergroup" and message.chat.id in FROM_GROUP_ID:
        chat_member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if chat_member.status in [types.ChatMemberOwner, types.ChatMemberAdministrator]:
            await forward_message_to_small_group(message, bot)
        else:
            msg = message
            await message.delete()
            await forward_message_to_small_group(msg, bot)

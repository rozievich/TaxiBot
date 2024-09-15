from aiogram import Bot, types

from data.config import TO_GROUP_ID
from .first_commans import mainrouter
from utils.misc import has_phone_number


async def forward_message_to_small_group(msg: types.Message, bot: Bot):
    await bot.send_message(chat_id=TO_GROUP_ID, text=f"<b>Message:</b> {msg.text}\n\n<b>Ism:</b> {msg.from_user.mention_html(msg.from_user.full_name)}\n<b>Username:</b> @{msg.from_user.username}\n<b>Guruh:</b> https://t.me/{msg.chat.username}")
    if has_phone_number(msg.text):
        await bot.send_message(chat_id=msg.chat.id, text=f"Telefon raqamingizni qoldirganingiz uchun rahmat #{msg.from_user.full_name}\nSizning zakazingiz shafyorlar 🚖 guruhiga tushdi ✅\nLichkada ishonchli shafyorlarimiz kutmoqda❗️\n\nGuruh sizga maqul bo'lsa do'stlaringizga ulashing\n@{msg.chat.username}")
    else:    
        await bot.send_message(chat_id=msg.chat.id, text=f"Assalomu alaykum #{msg.from_user.full_name}\nSizning zakazingiz shafyorlar 🚖 guruhiga tushdi ✅\nLichkada ishonchli shafyorlarimiz kutmoqda❗️\n\nAgar oson buyurtma bermoqchi bo'lsangiz shunchaki telefon raqmingizni yozib qoldiring ✍️\n\nGuruh sizga maqul bo'lsa do'stlaringizga ulashing\n@{msg.chat.username}")


@mainrouter.message()
async def handle_big_group_messages(message: types.Message, bot: Bot):
    if message.chat.type == "supergroup":
        chat_member = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if chat_member.status not in ["creator", "administrator"] and message.from_user.username != "GroupAnonymousBot":
            msg = message
            await message.delete()
            await forward_message_to_small_group(msg, bot)

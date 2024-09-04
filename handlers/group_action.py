from aiogram import Bot, types

from data.config import FROM_GROUP_ID, TO_GROUP_ID, KEYBOARDS
from .first_commans import mainrouter


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
            msg = message
            await message.delete()
            await bot.send_message(chat_id=TO_GROUP_ID, text=f"<b>Message:</b> {msg.text}\n\n<b>Ism:</b> {msg.from_user.mention_html(msg.from_user.full_name)}\n<b>Username:</b> @{msg.from_user.username}\n<b>Guruh:</b> https://t.me/{msg.chat.username}")

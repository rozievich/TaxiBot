from aiogram import Bot, types

from data.config import FROM_GROUP_ID, TO_GROUP_ID, KEYBOARDS
from .first_commans import mainrouter


async def forward_message_to_small_group(message: types.Message, bot: Bot):
    await bot.forward_message(chat_id=TO_GROUP_ID, from_chat_id=FROM_GROUP_ID, message_id=message.message_id)
    await message.delete()


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
    if message.chat.type == "supergroup" and message.chat.id == FROM_GROUP_ID:
        if await message_contains_keyword(message=message.text):
            await forward_message_to_small_group(message, bot)

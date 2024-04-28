from aiogram import Bot, types
from data.config import FROM_GROUP_ID, TO_GROUP_ID
from .first_commans import users_router


async def forward_message_to_small_group(message: types.Message, bot: Bot):
    try:
        await bot.forward_message(chat_id=TO_GROUP_ID, from_chat_id=FROM_GROUP_ID, message_id=message.message_id)
        await message.delete()
    except:
        pass


@users_router.message()
async def handle_big_group_messages(message: types.Message, bot: Bot):
    if message.chat.type == "group":
        await forward_message_to_small_group(message, bot)

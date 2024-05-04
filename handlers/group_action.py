from aiogram import Bot, types, F

from data.config import FROM_GROUP_ID, TO_GROUP_ID, KEYBOARDS
from keyboards.inline.user_button import button
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


@mainrouter.message(F.new_chat_member)
async def member_joined(message: types.Message):
    if message.new_chat_members:
        new_member = message.new_chat_members[0]
        await message.reply(
            f"Assalomu alaykum {new_member.full_name} 🤖\n"
            f"Bizning bot orqali tez va oson taxi toping ✅\n\n"
            f"Pastdagi ➕ tugmasini bosing va foydalanishni boshlang 🎛",
            reply_markup=button
        )


@mainrouter.message()
async def handle_big_group_messages(message: types.Message, bot: Bot):
    if message.chat.type == "supergroup" and message.chat.id == FROM_GROUP_ID:
        if await message_contains_keyword(message=message.text):
            await forward_message_to_small_group(message, bot)

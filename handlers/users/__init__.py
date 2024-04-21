from aiogram import Router
from aiogram.filters import CommandStart, Command
from .first_commans import start_command, help_command, panel_command
from .group_action import handle_big_group_messages

user_router = Router()


user_router.message.register(start_command, CommandStart())
user_router.message.register(help_command, Command('help'))
user_router.message.register(panel_command, Command('panel'))
user_router.message.register(handle_big_group_messages)

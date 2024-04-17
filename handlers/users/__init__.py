from aiogram import Router
from aiogram.filters import CommandStart, Command
from .search import start_command, help_command

user_router = Router()


user_router.message.register(start_command, CommandStart())
user_router.message.register(help_command, Command('help'))
